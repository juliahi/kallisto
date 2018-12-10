
/* 
 * File:   stats.cpp
 * Author: julia
 * 
 * Created on November 25, 2016, 7:38 PM
 */

#include "stats.h"

std::vector<int> countContigs(  KmerIndex& index, std::vector< std::pair<KmerEntry,int> >& v) {
  if (v.empty()) {
    return {};
  }
  sort(v.begin(), v.end(), [&](std::pair<KmerEntry, int> a, std::pair<KmerEntry, int> b)
       {
         if (a.first.contig==b.first.contig) {
           return a.second < b.second;
         } else {
           return a.first.contig < b.first.contig;
         }
       }); // sort by contig, and then first position


  int ec = index.dbGraph.ecs[v[0].first.contig];
  int lastEC = ec;
  std::vector<int> u = index.ecmap[ec];

  for (int i = 1; i < v.size(); i++) {
    if (v[i].first.contig != v[i-1].first.contig) {
      ec = index.dbGraph.ecs[v[i].first.contig];
      if (ec != lastEC) {
        u = index.intersect(ec, u);
        lastEC = ec;
        if (u.empty()) {
          return u;
        }
      }
    }
  }

  /*for (auto &x : vp) {
    //tmp = index.intersect(x.first,u);
    u = index.intersect(x.first,u);
    //if (!tmp.empty()) {
     // u = tmp;
      //count++; // increase the count
     // }
  }*/

  // if u is empty do nothing
  /*if (u.empty()) {
    return u;
    }*/

  // find the range of support
  int minpos = std::numeric_limits<int>::max();
  int maxpos = 0;

  for (auto& x : v) {
    minpos = std::min(minpos, x.second);
    maxpos = std::max(maxpos, x.second);
  }

  if ((maxpos-minpos + k) < min_range) {
    return {};
  }

  return u;
};

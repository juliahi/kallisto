#ifndef STATS_H
#define STATS_H
#include "common.h"
#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <unordered_map>



#include "MinCollector.h"

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/* 
 * File:   stats.h
 * Author: julia
 *
 * Created on November 25, 2016, 7:38 PM
 */


std::vector<int> countContigs(std::vector< std::pair<KmerEntry,int> >& v) const;


#endif /* STATS_H */

//
//  test.hpp
//  Bitonic
//
//  Created by Nathan Liccardo on 9/12/17.
//  Copyright © 2017 Nathan Liccardo. All rights reserved.
//

#ifndef bitonic_hpp
#define bitonic_hpp

#include <algorithm>
#include <stdlib.h>
#include <stdio.h>
#include <cmath>
#include "mpi.h"

using namespace std;


void printArray(int array[], int size);
bool checkChange(int i, int j);

#endif /* bitonic_hpp */

//
//  test.cpp
//  Bitonic
//
//  Created by Nathan Liccardo on 9/12/17.
//  Copyright © 2017 Nathan Liccardo. All rights reserved.
//

#include "bitonic.hpp"

int main(int argc, char ** argv) {
    
    MPI_Init(&argc, &argv);
    int rank, nb_instance;
    MPI_Comm_rank(MPI_COMM_WORLD, &rank);
    MPI_Comm_size(MPI_COMM_WORLD, &nb_instance);
    MPI_Status status;
    
    int cnodes = nb_instance-1;
    int n = cnodes*2;
    int values[3];
    
    if (n == 16) {
        if (rank == 0) {
            //int A[] = {14,16,15,11,9,8,7,5, 4,2,1,3,6,10,12,13};
            //int A[] = {1, 4, 6, 8, 4, 5, 3, 2};
            //int A[] = {9, 8, 6, 3, 1, 2, 5, 7};
            //int A[] = {3, 5, 8, 9, 10, 12, 14, 15};
            //int A[] = {95, 90, 60, 40, 35, 23, 18, 0};
            int A[] = {95, 90, 60, 40, 35, 23, 18, 0, 3, 5, 8, 9, 10, 12, 14, 15};
            
            
            int middle = n;
            int counter = 1;
            int process = 1;
            for (int i = 0; i < log2(n); i++) {
                middle = middle/2;
                
                // Send every tuples
                for (int j = 0; j < counter; j++) {
                    for (int k = 0; k < middle; k++) {
                        values[2] = (middle*2*j)+k;
                        values[0] = A[values[2]];
                        values[1] = A[values[2]+middle];
                        for (int l = 0; l < 3; l++)
                            MPI_Send(&values[l], 1, MPI_INT, process, 0, MPI_COMM_WORLD);
                        process += 1;
                    }
                }
                
                // Get every sorted tuples
                for (int j = 1; j < nb_instance; j++) {
                    for (int k = 0; k < 3; k++)
                        MPI_Recv(&values[k], 1, MPI_INT, j, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
                    A[values[2]] = values[0];
                    A[values[2]+middle] = values[1];
                }
                process = 1;
                counter *= 2;
            }
            printArray(A,n);
            
        }else {
            
            for (int i = 0; i < log2(n); i++) {
                
                for (int j = 0; j < 3; j++)
                    MPI_Recv(&values[j], 1, MPI_INT, 0, MPI_ANY_TAG, MPI_COMM_WORLD, &status);
                
                if (checkChange(values[0], values[1]))
                    swap(values[0],values[1]);
                
                for (int j = 0; j < 3; j++)
                    MPI_Send(&values[j], 1, MPI_INT, 0, 0, MPI_COMM_WORLD);
            }
            
        }
    }

    MPI_Finalize();
    
    return 0;
}

void printArray(int array[], int size) {
    printf("Array : ");
    for (int i = 0; i < size-1; i++) printf("%d, ", array[i]);
    printf("%d \n", array[size-1]);
}

bool checkChange(int i, int j) {
    if (i > j) return true;
    return false;
}


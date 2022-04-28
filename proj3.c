#include <stdio.h>

int classes[12][2] = {

    {4587, 4},

    {4599, 3},

    {8997, 1},

    {9696, 5},

    {4580, 3},

    {4581, 4},

    {4582, 2},

    {4583, 2},

    {3587, 4},

    {4519, 3},

    {6997, 1},

    {9494, 3}

};



const char *prefix[12] = {"MAT 236", "COP 220", "GOL 124", "COP 100", "MAT 230", "MAT 231", "MAT 232", "MAT 233", "MAT 256", "COP 420", "GOL 127", "COP 101"};

float costPerCredit = 120.25;

char runBool = 'Y';



int inputs(int *studIDptr, int *nbrCoursesptr) {

    printf("Enter the Students Id\n");

    scanf("%d", studIDptr);

    printf("Enter how many courses-up to 3\n");

    scanf("%d", nbrCoursesptr);

    return 0;

}//end inputs



char* getFooter(char* footerZero) {

    return footerZero;

}//end getFooter



void getHeader(char* headerFunc, int studIDFunc, int cost, char* heads) {

    printf("%s%d\n\n", headerFunc, studIDFunc);

    printf("1 credit hour = $%.2d\n\n", cost);

    printf("%s\n", heads);

}



void printCourses(int element) {

    printf("%d\t%s\t\t\t%d\t\t\t$%.2f\n", classes[element][0], prefix[element], classes[element][1], classes[element][1] * costPerCredit);

}



int main(int argc, const char * argv[]) {

    char header[] = ("VALENCE COMMUNITY COLLEGE\nORLANDO FL 10101\n*******************************\n\nFee Invoice Prepared for Student V");

    char footer[] = ("\t\tHealth & id fees\t\t\t$35\n\n-------------------------------------\n");

    char colheads[] = ("CRN\t\tCR_PREFIX\t\tCR_HOURS\n");

    int courseIdOne = 0;

    int courseIdTwo = 0;

    int courseIdThree = 0;

    

    int studID = 0;

    int nbrCourses = 0;

    while(runBool == 'y' || runBool == 'Y') {

    inputs(&studID, &nbrCourses);

    AGAIN: if(nbrCourses <= 3) {

        switch(nbrCourses) {

            case 0:

                getHeader(header, studID, costPerCredit, colheads);

                printf("%s", getFooter(footer));

                break;

            case 1:

                printf("Enter the course number: \n");

                scanf("%d", &courseIdOne);

                for(int i = 0; i < sizeof(classes); i++) {

                    if(courseIdOne == classes[i][0]) {

                        getHeader(header, studID, costPerCredit, colheads);

                        printCourses(i);

                        printf("%s", getFooter(footer));

                        printf("\tTotal Payments\t\t\t\t\t$%.2f\n", (classes[i][1] * costPerCredit) + 35);

                        goto BREAK_ONE;

                        //return 0;

                    }//end if

                }//end for

                

                printf("Sorry, invalid entry\n");

                BREAK_ONE:break;

            case 2:

                printf("Enter the two course numbers (xxxx xxxx): \n");

                scanf("%d %d", &courseIdOne, &courseIdTwo);

                for(int i = 0; i < sizeof(classes); i++) {

                    if(courseIdOne == classes[i][0]) {

                        for(int j = 0; j < sizeof(classes); j++) {

                            printf ("%d",(classes[i][1] + classes[j][1]));

                            if (courseIdTwo == classes[j][0]) {

                                if (classes[i][1] + classes[j][1] <= 7) {

                                getHeader(header, studID, costPerCredit, colheads);

                                printCourses(i);

                                printCourses(j);

                                printf("%s", getFooter(footer));

                                printf("\tTotal Payments\t\t\t\t\t$%.2f\n", (classes[i][1] * costPerCredit) + (classes[j][1] * costPerCredit) + 35);

                                goto BREAK_TWO;

                                //eturn 0;

                                }

                                else {

                                    printf("Sorry we can't process more than 7 credit hours! \n");

                                    goto BREAK_TWO;

                                }

                            }//end inner if



                        }//end inner for

                    }//end if

                    

                }//end for

            printf("Sorry, invalid entry\n");

            BREAK_TWO:break;

            case 3:

                printf("Enter the three course numbers (xxxx xxxx xxxx):\n");

               scanf("%d %d %d", &courseIdOne, &courseIdTwo, &courseIdThree);

                for(int i = 0; i < sizeof(classes); i++) {

                    if(courseIdOne == classes[i][0]) {

                        for(int j = 0; j < sizeof(classes); j++) {

                            if(courseIdTwo == classes[j][0]) {

                                for(int k = 0; k < sizeof(classes); k++) {

                                    if(courseIdThree == classes[k][0]) {

                                        if (classes[i][1] + classes[j][1] + classes[k][1] <= 7) {

                                        getHeader(header, studID, costPerCredit, colheads);

                                        printCourses(i);

                                        printCourses(j);

                                        printCourses(k);

                                        printf("%s", getFooter(footer));

                                        printf("\tTotal Payments\t\t\t\t\t$%.2f\n", (classes[i][1] * costPerCredit) + (classes[j][1] * costPerCredit) + (classes[k][1] * costPerCredit) + 35);

                                        goto BREAK_THREE;

                                        //return 0;

                                        }

                                        else {

                                            printf("Sorry we can't process more than 7 credit hours! \n");

                                            goto BREAK_THREE;

                                        }

                                    }//end k innermost if




                                }//end k innermost for

                            }//end j middle if

                        }//end j middle for

                    }//end i outer if

                }//end i outer for

                

                printf("Sorry invalid crn(s)!\n");

                BREAK_THREE: break;

        }//end switch

        ANOTHER: printf("Would you like to print another invoice?\n");

        scanf("%c", &runBool);

        scanf("%c", &runBool);

        if ((runBool != 'y' && runBool != 'Y') && (runBool != 'n' && runBool != 'N')) {

            printf("Invalid entry (it has to be y or n) \n");

            goto ANOTHER;

        }

    }//end if

    else {

        printf("Invalid number of courses(up to 3)\n");

        scanf("%d", &nbrCourses);

        goto AGAIN;

    }//end else

    

    }//end while

    printf("Goodbye!");

    return 0;

}//end main
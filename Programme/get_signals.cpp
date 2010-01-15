//////////////////////////////////////////////////////////////////////////////

#include <fstream>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>

using namespace std;

int get_word(ifstream* file,int* dataword)
{
   // This function reads 16 bit from the file and stores it in (*dataword).
   // The return value is 0 for fail and 1 for success.

   char databyte1,databyte2;
   int retval,datawordhelp;

   if ((*file).get(databyte1)) {
      if ((*file).get(databyte2)) {
         (*dataword)=0;
         (*dataword)=(*dataword) ^ (databyte2 << 8);
         datawordhelp=databyte1 & 0x000000ff;
         (*dataword)=(*dataword) ^ datawordhelp;
         (*dataword)=(*dataword) & 0x0000ffff;
         retval=1;
      } else {
         retval=0;
      }
   } else {
      retval=0;
   }

   if ((*dataword)>32767) {
      (*dataword)=(65536-(*dataword));
   }

   return retval;
}

int find_signals(char* filename,vector<int>* signals)
{
   int dataword,count;
   int statusold,statusnew,barrier1,barrier2,totzeit,lasttick;

   barrier1=2500;
   barrier2=700;
   totzeit=20;

   ifstream fin(filename,ios_base::binary);

   (*signals).clear();

   count=0;
   lasttick=-2*totzeit;
   statusold=0;
   while (get_word(&fin,&dataword)) {
      if (statusold==0) {
         if (dataword>barrier1) { statusnew=1; } else { statusnew=0; };
      } else {
         if (dataword>barrier2) { statusnew=1; } else { statusnew=0; };
      }
      if (statusnew!=statusold) {
         if ((statusnew==1) && (count-lasttick>totzeit)) {
	         (*signals).push_back(count);
	         lasttick=count;
         }
         statusold=statusnew;
      }
      count++;
   }

   fin.close();

   return 1;
}

int main(int argc,char *argv[])
{
   int i;
   vector<int> signals;

   if (argc!=2) {
      printf("Wrong number of arguments!\n");
      printf("Usage : %s filename\n",argv[0]);
      exit(0);
   }

   find_signals(argv[1],&signals);
   for (i=0;i<signals.size();i++) {
      printf("%f\n",(double)signals[i]/(double)44100);
   }

  return 0;
}

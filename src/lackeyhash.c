#include "lackeyhash.h"

extern int c_get_file_hash(char *filepath)
{
   FILE *fp = fopen(filepath, "rb");
   if (fp == NULL)
      return 0;

   long f1, f2 = 0;
   char c = 0;
   int sum = 0;
   do
   {
      f1 = f2;
      c = fgetc(fp);
      f2 = ftell(fp);
      if (c != 10 && c != 13)
         sum += (unsigned int)c;
      sum = sum % 100000000;
   } while (f1 != f2);

   fclose(fp);
   return sum;
}
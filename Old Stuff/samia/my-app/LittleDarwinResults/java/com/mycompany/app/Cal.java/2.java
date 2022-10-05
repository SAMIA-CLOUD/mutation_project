/* LittleDarwin generated order-1 mutant
mutant type: RelationalOperatorReplacement
----> before:          for (int i = month1 + 1; i <= month2-1; i++)
----> after:          for (int i = month1 + 1; i > month2-1; i++)
----> line number in original file: 22
----> mutated node: 192

*/

package com.mycompany.app;
import java.io.*;
public class Cal
{
   public static int cal (int month1, int day1, int month2,
                          int day2, int year)
   {
      int numDays;
      if (month2 == month1) // in the same month
         numDays  = day2 - day1;
      else
      {
         int daysIn[] = {0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
         int m4 = year % 4;
         int m100 = year % 100;
         int m400 = year % 400;
         if ((m4 != 0) || ((m100 == 0) && (m400 != 0)))
            daysIn[2] = 28;
         else
            daysIn[2] = 29;
         numDays = day2 + (daysIn[month1] - day1);
         for (int i = month1 + 1; i > month2-1; i++)
            numDays = daysIn[i] + numDays;
      }
      return (numDays);
   }

   }

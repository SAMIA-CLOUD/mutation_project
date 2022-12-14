/*
 * This file was automatically generated by EvoSuite
 * Thu Dec 02 20:15:19 GMT 2021
 */

package com.mycompany.app;

import org.junit.Test;
import static org.junit.Assert.*;
import static org.evosuite.runtime.EvoAssertions.*;
import com.mycompany.app.Cal;
import org.evosuite.runtime.EvoRunner;
import org.evosuite.runtime.EvoRunnerParameters;
import org.junit.runner.RunWith;

@RunWith(EvoRunner.class) @EvoRunnerParameters(mockJVMNonDeterminism = true, useVFS = true, useVNET = true, resetStaticState = true, separateClassLoader = true, useJEE = true) 
public class Cal_ESTest extends Cal_ESTest_scaffolding {

  @Test(timeout = 4000)
  public void test0()  throws Throwable  {
      // Undeclared exception!
      try { 
        Cal.cal((-2482), (-2482), 0, (-2482), 200);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -2482
         //
         verifyException("com.mycompany.app.Cal", e);
      }
  }

  @Test(timeout = 4000)
  public void test1()  throws Throwable  {
      // Undeclared exception!
      try { 
        Cal.cal((-1), (-1), (-728), (-728), (-728));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // -1
         //
         verifyException("com.mycompany.app.Cal", e);
      }
  }

  @Test(timeout = 4000)
  public void test2()  throws Throwable  {
      int int0 = Cal.cal((-965), (-965), (-965), (-965), (-239));
      assertEquals(0, int0);
  }

  @Test(timeout = 4000)
  public void test3()  throws Throwable  {
      int int0 = Cal.cal(2, 620, (-1693), 2, (-1693));
      assertEquals((-590), int0);
  }

  @Test(timeout = 4000)
  public void test4()  throws Throwable  {
      // Undeclared exception!
      try { 
        Cal.cal(181, 181, 37, 181, 0);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 181
         //
         verifyException("com.mycompany.app.Cal", e);
      }
  }

  @Test(timeout = 4000)
  public void test5()  throws Throwable  {
      // Undeclared exception!
      try { 
        Cal.cal(1, 204, 400, 400, 4);
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 13
         //
         verifyException("com.mycompany.app.Cal", e);
      }
  }

  @Test(timeout = 4000)
  public void test6()  throws Throwable  {
      int int0 = Cal.cal(7, 1, 1, 7, 1533);
      assertEquals(37, int0);
  }

  @Test(timeout = 4000)
  public void test7()  throws Throwable  {
      int int0 = Cal.cal(1, (-916), 1, 101, 29);
      assertEquals(1017, int0);
  }

  @Test(timeout = 4000)
  public void test8()  throws Throwable  {
      // Undeclared exception!
      try { 
        Cal.cal(13, 13, 0, 13, (-1800));
        fail("Expecting exception: ArrayIndexOutOfBoundsException");
      
      } catch(ArrayIndexOutOfBoundsException e) {
         //
         // 13
         //
         verifyException("com.mycompany.app.Cal", e);
      }
  }

  @Test(timeout = 4000)
  public void test9()  throws Throwable  {
      Cal cal0 = new Cal();
  }
}

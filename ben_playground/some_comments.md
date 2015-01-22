As of the commit I have today, I think I might have code to find the number of steps, but I would want some additional numbers to test this on (without having to figure out which one is the largest yet)

Using 3-2i and 2 + i

complex_1 = 3-2i
complex_2 = 2 + i

To divide them, my method returns:

4/5-7/5i

Then to round them, which will equate to q in http://mathforum.org/library/drmath/view/67068.html, my method returns:

1-1i 

q = 1 - 1i

Then, according to the mathforum information, the remainder should be

a-(q*b)
(3-2i) - (1-1i)(2+i)
(3-2i) - (3-1i)
0-1i

remainder = 0-1i

THEN... I reassign

complex_1=complex_2 OR
complex_1 = 2 + i

complex_2 = remainder OR 

complex_2 = 0-1i

Then, I iterate using 2+i and 0-1i as the complex numbers

Here is stuff I print out to the screen for the problem set here and the steps to 0 is 2

%%%%%%%%%%%%%%%
Iteration number is 1
Current remainder (first iteration it should be nil)
Current first number is 3-2i
Current second number is 2+1i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 2
Current remainder (first iteration it should be nil)0-1i
Current first number is 2+1i
Current second number is 0-1i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
the method has identified the remainder as zero. The number of steps is:
2

HERE IS ONE FOR -155 + 34i and 135-14i)

%%%%%%%%%%%%%%%
Iteration number is 1
Current remainder (first iteration it should be nil)
Current first number is -155+34i
Current second number is 135-14i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 2
Current remainder (first iteration it should be nil)-20+20i
Current first number is 135-14i
Current second number is -20+20i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 3
Current remainder (first iteration it should be nil)-5+6i
Current first number is -20+20i
Current second number is -5+6i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 4
Current remainder (first iteration it should be nil)0-4i
Current first number is -5+6i
Current second number is 0-4i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 5
Current remainder (first iteration it should be nil)-1-2i
Current first number is 0-4i
Current second number is -1-2i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
%%%%%%%%%%%%%%%
Iteration number is 6
Current remainder (first iteration it should be nil)0+1i
Current first number is -1-2i
Current second number is 0+1i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
the method has identified the remainder as zero. The number of steps is:
6
%%%%%%%%%%%%%%%
Iteration number is 6
Current remainder (first iteration it should be nil)0+1i
Current first number is -1-2i
Current second number is 0+1i
all math/assignment for this iteration will now happen
$$$$$$$$$$$$$$$$
the method has identified the remainder as zero. The number of steps is:
6
"""
 ******************************************************************************
 *  Purpose: Stopwatch Program for measuring the time that elapses between the start and end clicks
 *
 *  @author  Harshad B
 *  @version 3.8
 *  @since   20/12/2020
 ******************************************************************************
"""
import time


class StopWatch:
    def get_ElapsedTime(self):
        """
            Description:Simulates the stopwatch
            :parameter: None
            :return: This function will return elapsed time
        """
        start = input("Press Enter a number  to start timer: ")  # starts the timer
        begin = time.time()
        stop = input("Press Enter to a number stops timer: ")  # stops the timer
        end = time.time()  # gets the time when user press enter
        elapsed = end - begin  # difference between timer started and user press enter
        elapsed = round(elapsed, 2)

        return elapsed


if __name__ == '__main__':
    while True:
        try:                                # throws exception if occurs
            timer = StopWatch()
            elapse_Time = timer.get_ElapsedTime()     # called stopwatch function
            print("Elapsed time is ", elapse_Time, "seconds")
            break
        except Exception:                       # catches exception if throws
            print("enter valid number")
            continue
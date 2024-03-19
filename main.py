import argparse
import contextlib
import datetime
import os
import random



@contextlib.contextmanager
def temporary_directory_change(path):
    # Save the current working directory
    original_path = os.getcwd()
    
    # Change to the new directory
    os.chdir(path)
    
    try:
        # Yield control to the block of code that needs to run in the new directory
        yield
    finally:
        # Always switch back to the original directory, even if an error occurs
        os.chdir(original_path)

def random_delta(delta: int) -> int:
    return random.randint(1, delta)

def main():
    parser = argparse.ArgumentParser(description="Colorizer of your GitHub commit map")
    parser.add_argument("-s", "--start",
                        type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
                        help="Set a start date, format '%Y-%m-%d'")
    parser.add_argument("-e", "--end",
                        type=lambda d: datetime.datetime.strptime(d, "%Y-%m-%d").date(),
                        help="Set a end date, format '%Y-%m-%d'")
    parser.add_argument("-w", "--week-depth",
                        type=int, 
                        default=1,
                        choices=[1, 2, 3, 4, 5, 6],
                        help="Set a level of week random delta")
    parser.add_argument("-c", "--color-depth",
                        type=int, 
                        default=2,
                        choices=[2, 3, 4, 5],
                        help="Set a level of color hightlight in one day")
    parser.add_argument("-c", "--check",
                        action="store_true",
                        help="Take a test pass")
    parser.add_argument("-p", "--path",
                        type=str,
                        help="Set a project path")
    args = parser.parse_args()

    end = args.end
    res_date = args.start
    if not res_date or not end:
        raise ValueError("Args --start and --end must be specified")
    assert res_date < end, "start date shoud be early end date"

    is_check = args.check
    week_depth_lvl = args.week_depth

    project_path = args.path
    if not os.path.isdir(project_path):
        raise ValueError("Incorrect path value set. Please check it")


    with temporary_directory_change(project_path):
        while res_date <= end:
            for i in range(random.randrange(1, 3)):
                git_command = f'git add . && git commit --date "{res_date}" -m "#{i} commit for {res_date}"'
                if not is_check:
                    with open("main", "a") as file:
                        file.write(f"\n{res_date} {i}")
                    os.system(git_command)
                else:
                    print(git_command)

            res_date += datetime.timedelta(days=random_delta(week_depth_lvl))

        if not is_check:
            os.system("git push")


if __name__ == "__main__":
    main()

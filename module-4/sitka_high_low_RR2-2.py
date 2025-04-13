#Rashai Robertson
#CSD-325
#04/06/2025
#Module 4 Assignment 4.2


#change 1-
def main():
    """
    Allows the user to select whether to view high or low temperatures, or exit.
    """
#Change: while loop to keep the program running until the user chooses to exit
    while True:
        print("\nSelect an option:")
        print("1. View High Temperatures")
        print("2. View Low Temperatures")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        # Change: moved highs to choice one and lows to choice two.
        if choice == "1":
            print("Displaying high temperatures...")
            import csv
            from datetime import datetime

            from matplotlib import pyplot as plt

            filename = 'sitka_weather_2018_simple.csv'
            with open(filename) as f:
                reader = csv.reader(f)
                header_row = next(reader)

                # Get dates and high temperatures from this file.
                dates, highs = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    high = int(row[5])
                    highs.append(high)

            # Plot the high temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            ax.plot(dates, highs, c='red')

            # Format plot.
            plt.title("Daily high temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
            
        
        elif choice == "2":
            print("Displaying low temperatures...")
            import csv
            from datetime import datetime

            from matplotlib import pyplot as plt

            filename = 'sitka_weather_2018_simple.csv'
            with open(filename) as f:
                reader = csv.reader(f)
                header_row = next(reader)

                #Change: Get dates and low temperatures from this file.
                dates, lows = [], []
                for row in reader:
                    current_date = datetime.strptime(row[2], '%Y-%m-%d')
                    dates.append(current_date)
                    low = int(row[6])
                    lows.append(low)

            # Plot the low temperatures.
            #plt.style.use('seaborn')
            fig, ax = plt.subplots()
            
            #Change: changed color to blue
            ax.plot(dates, lows, c='blue')

            # Format plot.
            plt.title("Daily low temperatures - 2018", fontsize=24)
            plt.xlabel('', fontsize=16)
            fig.autofmt_xdate()
            plt.ylabel("Temperature (F)", fontsize=16)
            plt.tick_params(axis='both', which='major', labelsize=16)
            plt.show()
           
        elif choice == "3":
            print("Exiting program...")
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()



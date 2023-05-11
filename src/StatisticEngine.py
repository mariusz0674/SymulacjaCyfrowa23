import matplotlib.pyplot as plt


class StatisticEngine:

    def __init__(self):
        self.userStatisticPackList = []
        self.activeUsersInTime = ()
        self.inQueForServiceUsersInTime = ()
        self.fig, (self.ax1, self.ax2, self.ax3) = plt.subplots(3, 1)


    def addActiveUsersInTime(self, time, usersCount):
        self.activeUsersInTime += ((time, usersCount),)

    def addInQueForServiceUsersInTime(self, time, usersCount):
        self.inQueForServiceUsersInTime += ((time, usersCount),)
    def appendUserStatisticPack(self, userStatisticPack):
        self.userStatisticPackList.append(userStatisticPack)

    def switchsByUsersHist(self):
        usersSwitches = []
        for userStatisticPack in self.userStatisticPackList:
            usersSwitches.append(userStatisticPack.baseSwitches)
        return usersSwitches

    def printActiveUsersInTime(self):
        x = [t[0] for t in self.activeUsersInTime]
        y = [t[1] for t in self.activeUsersInTime]
        self.ax1.plot(x, y)
        self.ax1.set_xlabel('time')
        self.ax1.set_ylabel('users')
        self.ax1.set_title('Active users in time')

    def printInQueForServiceUsersInTime(self):
        x = [t[0] for t in self.inQueForServiceUsersInTime]
        y = [t[1] for t in self.inQueForServiceUsersInTime]
        self.ax2.plot(x, y)
        self.ax2.set_xlabel('time')
        self.ax2.set_ylabel('users')
        self.ax2.set_title('In que for service users in time')

    def printSwitchBasesByUsersHist(self):
        values = self.switchsByUsersHist()
        self.ax3.hist(values, bins=50)
        self.ax3.set_xlabel('switches')
        self.ax3.set_ylabel('users')
        self.ax3.set_title('Histogram of switches by users')

    def showPlots(self):
        plt.subplots_adjust(hspace=1.0)
        plt.show()



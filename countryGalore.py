# Jasmine Campbell 250886086


# Create class Country
class Country:
    def __init__(self, name, pop, area, continent):
        self._name = str(name)
        self._pop = int(pop)
        self._area = float(area)
        self._continent = str(continent)

    # Make string rep. for Country
    def __repr__(self):
        return '{} in {}'.format(self._name, self._continent)

    def setPopulation(self, pop):
        self._pop = pop

    def getName(self):
        return self._name

    def getArea(self):
        return self._area

    def getPopulation(self):
        return self._pop

    def getContinent(self):
        return self._continent

    def getPopDensity(self):
        return float(self._pop / self._area)


# Create the class CountryCatalogue
class CountryCatalogue:
    def __init__(self, filename):
        infile = open('continent.txt', 'r')
        self._data = []
        self._count = []
        self._con = []
        self._cDictionary = {}
        self._countcat = []
        # Start doing dictionary
        for line in infile:
            self._data.append(line)
        # Get rid of the spare (title)
        self._data.pop(0)
        # Separate Country and continent into lists
        for line in self._data:
            self._nline = str(line).rstrip()
            n = self._nline.split(',')
            self._con.append(n[1])
            self._count.append(n[0])
        # Make dictionary - key is country: continent is value
        for i in range(len(self._count)):
            self._cDictionary[self._count[i]] = self._con[i]
        # Close the file!
        infile.close()
        # Now open the mysterious file
        file = open(filename, 'r')
        self._list = []
        for line in file:
            self._list.append(line)
        # Again get rid of the spare
        self._list.pop(0)
        # Time to create the catalogue (using list)
        for line in self._list:
            temp = str(line).rstrip().split('|')
            tempone = str(temp[1]).replace(',', '')
            pop = float(tempone)
            temptwo= str(temp[2]).replace(',', '')
            area= float(temptwo)
            density = '%.2f' %(pop/area)
            # Put them into new format - Name|Continent|Population|Density
            newfor = '{}|{}|{}|{}'.format(temp[0], self._cDictionary[temp[0]], pop, density)
            self._countcat.append(newfor)
        file.close()
    def __repr__(self):
        temp = str(self._countcat).replace('[', '').replace(']', '').replace("'", '').replace(', ', '\n')
        return temp

    # MAKE addCOUNTRY
    def addCountry(self):
        # Get user input
        newcountry = str(input("Please the country you would like to add: "))
        # Make sure the country doesn't already exist
        for i in range(len(self._countcat)):
            while str(self._countcat[i]).lower().startswith(newcountry.lower()):
                print('This country is already in the catalogue.')
                newcountry = str(input("Please add a country not inside catalogue: ")).lower()
        # Once verified get more info
        newpop = int(input('Please add a population for this country: '))
        newarea = float(input('Please add an area for this country: '))
        newdens = '%.2f' % (newpop/newarea)
        newcont = str(input('Please add a continent for this country: ')).lower()
        # Now format and add to Catalogue
        newpart = '{}|{}|{}|{}'.format(newcountry, newcont, newpop, newdens)
        self._countcat.append(newpart)
        self._cDictionary[newcountry] = newcont
        # Give a confirmation message
        return print('Your addition was successful.')

    # MAKE deleteCountry
    def deleteCountry(self):
        # Get input
        delcountry = str(input('Please enter the country you would like to delete: '))
        t = 0
        # Verify if country exists ^ use a marker for loop
        for i in range(len(self._countcat)-1):
            # Pop the value out if it exists and give message
            if str(self._countcat[i]).lower().startswith(delcountry.lower()):
                self._countcat.pop(i)
                t += 1
                return print('{} has been deleted.'.format(delcountry))
        # Analyze the marker for a return value
        if t == 0:
            return print('{} is not in catalogue.'.format(delcountry))

    # MAKE findCountry
    def findCountry(self):
        # Get input
        findcountry = str(input('Please input the country you would like to find:')).lower()
        t = 0
        # Make loop to find country ^ Use a marker
        for i in range(len(self._countcat)):
            temp = str(self._countcat[i]).lower().split('|')
            # Verify if country exists and if so display info
            if findcountry == temp[0]:
                t += 1
                final = self._countcat[i]
                return print('{}'.format(final))
        # If country is fake, display that it don't exist
        if t == 0:
            return print("The country doesn't exist in the catalogue.")

    # MAKE filterCountriesByContinent
    def filterCountriesByContinent(self):
        # Get input
        contin = str(input('Please enter continent to use as a filter: '))
        # Make temporary list for countries
        fil = []
        # Check to see what countries fit
        for i in range(len(self._countcat)):
            temp = str(self._countcat[i]).split('|')
            if contin.lower() == temp[1].lower():
                fil.append(temp[0])
        # Check to see if empty, display message
        if fil == []:
            return print('There are no countries in {}'.format(contin))
        else:
            final = str(fil).replace('[', '').replace(']', '').replace("'", '')
            return print('The countries in {} are {}.'.format(contin, final))

    # MAKE printCountryCatalogue
    def printCountryCatalogue(self):
        t = self.__repr__()
        return print(t)

    # MAKE setPopulationOfASelectedCountry
    def setPopulationOfASelectedCountry(self):
        # Get input
        coun = str(input('Please enter the country you would like to set a population to: ')).lower()
        n = 0
        # Go through catalogue and find country ^ Use marker
        for i in range(len(self._countcat)):
            # If found change specified value and return message
            if str(self._countcat[i]).lower().startswith(coun):
                newpop = input('Please enter the new population: ')
                temp = str(self._countcat[i]).split('|')
                area = float(temp[2])/float(temp[3])
                d = float(newpop)/area
                newdens = '% .2f'% d
                self._countcat.insert(i,str(self._countcat[i]).replace(temp[2], newpop).replace(temp[3], str(newdens)))
                self._countcat.pop(i+1)
                n += 1
                return print('The new population density for {} is {}'.format(coun, newdens))
        # Check marker
        if n == 0:
            return print('There is no country with the name, {}.'.format(coun))

    # MAKE findCountrywithLargestPop
    def findCountryWithLargestPop(self):
        l = 0
        # Go through catalogue for populations
        for i in range(len(self._countcat)):
            temp = str(self._countcat[i]).split('|')
            num = float(temp[2])
            # Always store the larger number
            if num > l:
                l = num
        # Now find which country the largest pop belongs too
        for line in self._countcat:
            step = str(line).split('|')
            numtwo = float(step[2])
            # Once found, give message
            if l == numtwo:
                return print('{} has the largest population with {} people.'.format(step[0], step[2]))

    # Make findCountryWithSmallestArea
    def findCountryWithSmallestArea(self):
        # Just start with the first area and go from there
        min = str(self._countcat[0]).split('|')
        # Get area from density
        min = float(min[2])/float(min[3])
        # Now check this value to how the other are
        for i in range(len(self._countcat)):
            temp = str(self._countcat[i]).split('|')
            num = float(temp[2])/float(temp[3])
            # If it's smaller than the original min, store it
            if num <= float(min):
                min = num
        # Now find which country the min belongs too. Return a message
        for line in self._countcat:
            step = str(line).split('|')
            numtwo = float(step[2])/float(step[3])
            if min == numtwo:
                numtwo = '%.2f' % numtwo
                return print('{} has the smallest area with it being {}.'.format(step[0], numtwo))

    # MAKE filterCountriesByPopDensity
    def filterCountriesByPopDensity(self):
        # First, set the boundaries and make a temporary list
        lower = int(input('Please enter lower bound for density filter: '))
        upper = int(input('Please enter upper bound for density filter: '))
        countrylist = []
        # Go through and store the density that fits in the boundaries
        for line in self._countcat:
            temp = str(line).split('|')
            density = float(temp[3])
            if lower < density < upper:
                countrylist.append(temp[0])
        # Now give the message with the countries
        countrylist = str(countrylist).replace('[', '').replace(']', '').replace("'", '')
        return print('The countries within the parameters are {}'.format(countrylist))

    # MAKE findMostPopulousContinent
    def findMostPopulousContinent(self):
        # Set values to start at zero
        northnum = 0
        asianum = 0
        southnum = 0
        africanum = 0
        europenum = 0
        # Now check which value fits where and add it to proper continent
        for line in self._countcat:
            temp = str(line).lower().split('|')
            if temp[1] == 'north america':
                northnum += float(temp[2])
            if temp[1] == 'asia':
                asianum += float(temp[2])
            if temp[1] == 'south america':
                southnum += float(temp[2])
            if temp[1] == 'africa':
                africanum += float(temp[2])
            if temp[1] == 'europe':
                europenum += float(temp[2])
        # Now get back the top number
        topnum = max(northnum,southnum,asianum,africanum,europenum)
        # Go through and find matching continent
        if topnum == northnum:
            return print('The most populous continent is North America with {} people.'.format(northnum))
        if topnum == asianum:
            return print('The most populous continent is Asia with {} people.'.format(asianum))
        if topnum == southnum:
            return print('The most populous continent is South America with {} people.'.format(southnum))
        if topnum == africanum:
            return print('The most populous continent is Africa with {} people.'.format(africanum))
        if topnum == europenum:
            return print('The most populous continent is Europe with {} people.'.format(europenum))

    # Make saveCountryCatalogue
    def saveCountryCatalogue(self, filename):
        # Alphabetize the catalogue
        self._countcat.sort()
        # Open the file you want content saved to
        infile = open(filename,'w')
        # Give it the title back
        infile.write('Name|Continent|Population|Population Density \n')
        # Add each line and then close it.
        for line in self._countcat:
            infile.write('{} \n'.format(line))
        infile.close()
        # Give message that it has been done
        return print('{} has been saved'.format(filename))

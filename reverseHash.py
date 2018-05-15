'''
Author  : RituRaj 
Date    : May 15, 2018 
'''

class Hash:
    
    letters = "acdegilmnoprstuw"

    def hash(self,s):
        """
        This function takes string as an argument and converts it into 
        hash number using the characters in the letters variable.
        :param self - class instance
        :param s - string
        :return hash of the input string
        """
        h=7
        for i in s:
            h = (h*37 + self.letters.index(i))
        return h

    def reverseHash(self,num):
        """
        This function is reverse of the above function (hash), 
        takes integer as an argument and converts it into string.
        :param self - class instance
        :param num - integer
        :return reverse of the above function(hash)
        """
        h = 7
        s = ''
        while num > h:
            pos = num % 37
            s += self.letters[pos]
            num = num / 37
        return s[::-1]


def main():
    obj = Hash()
    print "Calling reverseHash(680131659347)"
    sample_dh = obj.reverseHash(680131659347)
    print sample_dh
    print '\n'
    print "Calling hash(leepadg)"
    sample_h = obj.hash("leepadg")
    print sample_h

if __name__ == '__main__':
    main()
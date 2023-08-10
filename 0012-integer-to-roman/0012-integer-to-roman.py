class Solution:
    def intToRoman(self, num: int) -> str:
        #define values + symbols for roman numerals
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        numerals = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        roman_numeral = ''

        for value, numeral in zip(values, numerals): #iterate over e/ value and number in parallel
            count = num // value # determine the number of numeral repetitions
            roman_numeral += numeral * count #append numeral "count" times to the result
            num -= value * count #decrease the number by 'value' * 'count'
        return roman_numeral 



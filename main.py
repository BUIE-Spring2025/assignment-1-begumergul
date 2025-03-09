def int_to_roman(num):
    if 1 <= num<= 3999:
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        roman_version= ''
        for i in range(len(values)):
            while num >= values[i]: 
                roman_version += symbols[i]
                num -= values[i]
        return roman_version
    else:
        return 'Value must be between 1 and 3999'

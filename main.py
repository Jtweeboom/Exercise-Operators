# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

#1 The language spoken the most in Switzerland is the same as in Spain
Spain_language="spanish"
Switzerland_language="german"
print(Spain_language == Switzerland_language)

#2 The most prevalent religion in Switzerland is the same as in Spain
Spain_religion='Roman Catholic'
Switzerland_religion='Roman Catholic'
print(Spain_religion == Switzerland_religion)

#3 The name length of Spain's capital does not equal that of Switzerland
name_length_capital_spain=len("madrid")          
name_lenght_capital_switzerland=len("bern")     
print(name_length_capital_spain != name_lenght_capital_switzerland)

#4 Switzerland's GDP is greater than Spain's GDP.
gdp_spain=1714860000000             #dollar
gdp_switzerland=59071000000000000   #dollar
print(gdp_switzerland>gdp_spain)

#5 The population growth is less than 1% in Switzerland and Spain.
population_growth_spain= -0.03                 #procent
population_growth_switzerland=0.65             #procent
percentage_growth=1                            #procent
print(population_growth_spain and population_growth_switzerland < percentage_growth)

#6 At least one of the two countries has a population count of over 10 million.
population_count_spain=47260584
population_count_switzerland=8453550
population_count_over=10000000
print(population_count_spain > population_count_over or population_count_switzerland > population_count_over)

#7 Exactly one of the two countries has a population count of over 10 million.
if ((population_count_spain>population_count_spain) and (population_count_switzerland <population_count_over)) or (population_count_spain<population_count_over) and (population_count_switzerland>population_count_over): Exactly_one_of_the_two_has_population_count_of_over_10_milion = True
else: Exactly_one_of_the_two_has_population_count_of_over_10_milion = False





if ((population_count_spain > population_count_over) and (population_count_switzerland < population_count_over)) or ((population_count_spain < population_count_over) and (population_count_switzerland > population_count_over)): 
 Exactly_one_of_the_two_has_population_count_of_over_10_milion = True
else: Exactly_one_of_the_two_has_population_count_of_over_10_milion =  False

print(Exactly_one_of_the_two_has_population_count_of_over_10_milion)
formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four") 
print formatter % (True, False, False, True)
#printer formatteren fire ganger
print formatter % (formatter, formatter, formatter, formatter)
#printer formatter med verdiene under, på en linje pga komma. kommer med dobbel " på nest siste linje pga "didn't"
print formatter % (
"I had this thing.",
"That you could type up right.",
"But it didn't sing.",
"So I said goodnight."
)
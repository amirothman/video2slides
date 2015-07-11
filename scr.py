script = open('script_for_copying','w')
script.write('#!/bin/bash\n')

for i in range(100):
  script.write(str(i)+'\n')
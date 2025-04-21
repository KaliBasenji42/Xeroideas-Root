import os

# Variables

run = True

instructions = [
  'Input "quit" to quit',
  'Input "?" to reprint this',
  'Input "temp" to update template marked areas'
]

paths = []
exts = [
  '.html'
]

location = './'

# Template

templatePath = 'template.html'
templateCont = []
template = []
tempStart = '<!--Start-->\n'
tempEnd = '<!--End-->\n'

projectId = '{project}'
projectDepth = len('projects/') # What to cut off in front of Project

# Simple Functions

def cutStringAt(string, char):
  
  for i in range(len(string)):
    
    if string[i] == char: return string[:i]
    
  
  return string
  

def remFile(string):
  
  for i in range(len(string)):
    
    if string[-i] == '/': return string[:-i]
    elif string[-i] == '\\': return string[:-i]
    
  
  return ''
  

# Complex Functions

def getPaths():
  
  print('Getting file paths:\n')
  
  for root, directories, files in os.walk(location):
    
    for file in files:
      
      path = os.path.normpath(os.path.join(root, file))
      
      # HTML
      
      match = False
      
      for ext in exts:
        if path[-len(ext):] == ext: match = True
      
      if path == templatePath: match = False
      
      if match:
        
        try: 
          
          with open(path, 'r+', encoding='utf-8', errors='ignore') as file: pass
          
        except: print('Unable to open "' + path + '" :/')
        else:
            
          paths.append(path)
          print('Added "' + path + '" to paths')
          
        
      
    
  

def readTemplate():
  
  print('Reading Template:\n')
  
  try:
    
    with open(templatePath, 'r+', encoding='utf-8', errors='ignore') as file: templateCont = file.readlines()
    
  except:
    
    print('Unable to open Template :/')
    
    return False # Fail
    
  else:
    
    add = False
    
    cont = []
    
    for line in templateCont:
      
      if line == tempStart: add = True
      
      elif line == tempEnd:
        
        add = False
        
        template.append(cont)
        cont = []
        
      
      elif add: cont.append(line)
      
    
    for sect in template:
      
      print('Start')
      
      for line in sect: print(line, end='')
      
      print('End')
      
    
  
  return True # Success
  

def templateEdit():
  
  if input('Enter "y" to continue: ') != 'y': return
  
  print('\nWriting to Files:\n')
  
  for path in paths:
    
    cont = [] # Content of file before writing
    
    try:
      
      with open(path, 'r+', encoding='utf-8', errors='ignore') as file: cont = file.readlines()
      
    except: print('Unable to open "' + path + '" :/')
    
    else:
      
      addCont = True # If it should add content, not template section
      
      newCont = [] # Content to be writen to file
      
      sect = 0 # Template section
      
      project = cutStringAt(path[projectDepth:], '\\')
      
      # Start/End
      
      for line in cont:
        
        if line == tempEnd: # End of template section
          
          newCont.append(line)
          
          addCont = True
          
        
        elif line == tempStart: # Start of template section
          
          newCont.append(line)
          
          addCont = False
          
          newCont = newCont + template[sect] # Add template content
          
          sect += 1 # Iterate
          
          # Ignore old HTML file content
          
        
        elif addCont: newCont.append(line)
        # ^^^ Add old HTML file content
        
      
      # Replace Project Id
      
      for i in range(len(newCont)):
        
        line = newCont[i].replace(projectId, project)
        newCont[i] = line
        
        
      
      # Write to file
      
      with open(path, 'w', encoding='utf-8', errors='ignore') as file: file.writelines(newCont)
      
      # Print
      
      print('Updated "' + path + '" as Project "' + project + '"')
      
    
  

# Pre Loop

getPaths()

print()

for string in instructions: print(string)

# Input Loop

while run:
  
  print()
  inp = input('Input: ').lower()
  print()
  
  if inp == 'quit': run = False
  
  elif inp == '?':
    for string in instructions: print(string)
  
  elif inp == 'temp':
    
    if readTemplate():
      print()
      templateEdit()
    
  

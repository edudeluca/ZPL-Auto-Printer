# %%
import os
import zipfile
import time


# %%
# sets printer to be used
printerPort = r'\\192.168.0.26\zebraPrinter'

# gets python file path and the path to the files to be printed
pythonFolder = os.path.dirname(__file__)

printingFolderName = 'Etiquetas'
printingJobsFolder = os.path.join(pythonFolder,printingFolderName)

# creates folder to store pending jobs
try:
    os.makedirs(printingJobsFolder)
except FileExistsError:
    None

# %%
while True:
    pendingJobsFiles = os.listdir(printingJobsFolder)
    if '.txt' in [os.path.splitext(file)[1] for file in pendingJobsFiles]: 
        for file in pendingJobsFiles:
            fileExtension = os.path.splitext(file)[1]
            filePath = os.path.join(printingJobsFolder,file)
            # print(filePath)

            if fileExtension == '.txt':
                printCommand = f'copy "{filePath}" {printerPort}'
                print('printed: ', file)
                # os.system(printCommand)
                os.remove(filePath)
                
            
    else:
        if '.zip' in [os.path.splitext(file)[1] for file in pendingJobsFiles]:
            for file in pendingJobsFiles:
                fileExtension = os.path.splitext(file)[1]
                filePath = os.path.join(printingJobsFolder, file)
                
                if fileExtension == '.zip':
                    with zipfile.ZipFile(filePath,'r') as zip_ref:
                        zip_ref.extractall(printingJobsFolder)
                    print('unziped: ', file)
                    os.remove(filePath)
                    break
    
    time.sleep(1)




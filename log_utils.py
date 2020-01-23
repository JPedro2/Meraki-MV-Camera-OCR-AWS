import os

def write_to_reko_log_file(textDetections):
    if os.path.exists('rekognition_logs.txt'):
        with open('rekognition_logs.txt', 'a') as f:
            f.write("\nAnother Run\n----------\n")
        with open('rekognition_logs.txt', 'a') as f:
            for text in textDetections:
                f.write('Detected text: ' + text['DetectedText'])
                f.write('\n   Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                f.write('\n      Type: ' + text['Type'] + "\n \n")
            f.write('----------\n')
    else:
        with open('rekognition_logs.txt', 'w') as f:
            f.write("The Beggining of it all!\n----------\n")
            for text in textDetections:
                f.write('Detected text: ' + text['DetectedText'])
                f.write('\n   Confidence : ' + "{:.2f}".format(text['Confidence']) + "%")
                f.write('\n      Type: ' + text['Type'] + "\n \n")
            f.write('----------\n')
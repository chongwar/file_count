import PySimpleGUI as sg
import warnings
import os

warnings.filterwarnings('ignore')


def window():
    layout = [[sg.Text('Document to open', justification='center')],
              [sg.Input('Please choose a file:', key='file_name'), sg.FolderBrowse()],
              [sg.Checkbox('png', key='png'), sg.Checkbox('jpg', key='jpg'), 
               sg.Checkbox('bmp', key='mp4'), sg.Checkbox('mkv', key='mkv'),
               sg.Checkbox('pdf', key='pdf'), sg.Checkbox('txt', key='txt')],
              [sg.Text('Choose other format'), sg.Input('', key='other_format')],
              [sg.Button('Count', key='count'), sg.Exit()]]
        
    window = sg.Window('File counter', layout)
    window_1_active = False
    while True: 
        event, values = window.Read()
        if event in ['Exit', None]:
            break
        if event == 'count' and not window_1_active:
            path = values['file_name']
            
            formats = []
            for i in ['png', 'jpg', 'mp4', 'txt', 'pdf', 'mkv']:
                if values[i]:
                    formats.append(i)
            if values['other_format']:
                formats.append(values['other_format'])
            
            num = file_count(path, formats)
            window_1_active = True
            layout_1 = [[sg.Text('Total number is {}'.format(num))],
                        [sg.Exit()]]
            window_1 = sg.Window('Result', layout_1)
            
            while True:
                event_1, values_1 = window_1.Read()
                if event_1 in ['Exit', None]:
                    window_1.Close()
                    window_1_active = False
                    break
            

    
def file_count(path, formats, count_now=0):
    count = count_now
    file_names = os.listdir(path)
    for file_name in file_names:
        file_path_tmp = os.path.join(path, file_name)
        
        if os.path.isdir(file_path_tmp):
            count = file_count(file_path_tmp, formats, count_now=count)
        elif file_name.split('.')[-1] in formats:
            count += 1
    
    return count


if __name__ == "__main__":
    window()

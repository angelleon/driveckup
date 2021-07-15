from .file_repo import FileRepo
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
from io import FileIO


class Driveckup:
    def __init__(self, file_repo: FileRepo):
        self.f_repo = file_repo
        self.gauth = GoogleAuth()
        self.gauth.LocalWebserverAuth()
        self.drive = GoogleDrive(self.gauth)

    def backup_file(self, f, parent_id=None):
        print(f'Backuping file [{f}]')
        if parent_id is None:
            parent_id = 'root'
        if f is None:
            raise ValueError('Provided filename is None')
        f = self.f_repo.get(f)
        drive_f = self.drive.CreateFile({
            'title': f.name,
            'parents': [
                {
                    'kind': 'drive#fileLink',
                    'id': parent_id
                }
            ]
        })
        drive_f.SetContentFile(f.resolve())
        g = drive_f.Upload()
        print(g)

    def backup_directory(self, d, parent_id=None):
        print(f'backuping directory [{d}]')
        if parent_id is None:
            parent_id = 'root'
        d = self.f_repo.get_dir(d)
        drive_d = self.drive.CreateFile({
            'title': d.name,
            'parents': [
                {
                    'kind': 'drive#fileLink',
                    'id': parent_id
                }
            ],
            'mimeType': 'application/vnd.google-apps.folder'
        })
        # print(f'direcotry id [{drive_d["id"]}]')
        print(f'uploading [{d}]')
        drive_d.Upload()
        print(f'uploaded [{d}]')
        print(f'direcotry id [{drive_d["id"]}]')
        drive_d_id = drive_d["id"]
        for f in self.f_repo.get_dir_cont(d):
            if f.is_dir():
                self.backup_directory(f, drive_d_id)
                continue
            if not f.is_file():
                raise ValueError(f'{f} is not a file')
            self.backup_file(f, drive_d_id)



import syssys.path.append('..')import osimport shutilimport subprocessdef copy(src, dst):    if os.path.isfile(src):        shutil.copyfile(src, dst)    else:        shutil.copytree(src, dst)SERVER_FILES = ['maps', 'config.txt', 'scripts', 'web']REMOVE_EXTENSIONS = ['txtc', 'pyc']REMOVE_FILES = ['w9xpopen.exe']from pyspades.common import crc32version = crc32(open('../data/client.exe', 'rb').read())open('./dist/client_version', 'wb').write(str(version))open('./dist/run.bat', 'wb').write('run.exe\npause\n')for name in SERVER_FILES:    copy('../feature_server/%s' % name, './dist/%s' % name)for root, sub, files in os.walk('./dist'):    for file in files:        path = os.path.join(root, file)        if file in REMOVE_FILES:            os.remove(path)        else:            for ext in REMOVE_EXTENSIONS:                if file.endswith(ext):                    os.remove(path)                    break    def get_hg_rev():    pipe = subprocess.Popen(        ["hg", "log", "-l", "1", "--template", "{node}"],        stdout=subprocess.PIPE)    return pipe.stdout.read()[:12]filename = 'pyspades-feature_server-%s.zip' % get_hg_rev()try:    os.remove(filename)except OSError:    passsubprocess.check_call(['7z', 'a', filename, 'dist'])
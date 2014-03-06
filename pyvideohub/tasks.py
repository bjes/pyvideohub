from celery import Celery

app = Celery('tasks', broker='redis://localhost')

@app.task(name='tasks.convert_video')
def convert_video(cmd, options, dst_basedir, tmp_filename):
    import subprocess
    import os
    # 去掉開頭的 tmp-
    new_filename = tmp_filename[4:]
    src_ab_path = os.path.join(dst_basedir, tmp_filename)
    dst_ab_path = os.path.join(dst_basedir, new_filename)
    subprocess.call('{} {} -i {} {}'.format(cmd, options, src_ab_path, dst_basedir), shell=True)
    os.remove(src_ab_path)

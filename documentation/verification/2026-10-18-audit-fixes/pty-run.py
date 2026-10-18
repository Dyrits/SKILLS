import os, pty, sys, time
pid, fd = pty.fork()
if pid == 0:
    os.execvp("bash", ["bash", sys.argv[1]])
out = b""
for answer in [b"\n", b"y\n", b"boom\n"]:
    time.sleep(0.5); os.write(fd, answer)
time.sleep(0.5)
try:
    while True:
        chunk = os.read(fd, 4096)
        if not chunk: break
        out += chunk
except OSError:
    pass
_, status = os.waitpid(pid, 0)
print(out.decode().replace("\r", "")[-120:])
print("exit", os.waitstatus_to_exitcode(status))

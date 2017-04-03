# Tutorial

Concrete Process to add one vulnerability into [LinuxFlaw repo](https://github.com/mudongliang/LinuxFla):

1. Upload the vulnerable programs onto [source-packages repo](https://github.com/mudongliang/source-packages);
2. Upload poc to [LinuxFlaw repo](https://github.com/mudongliang/LinuxFlaw). P.S. you can download most pocs from [exploit-database repo](https://github.com/offensive-security/exploit-database/);
3. Test the poc in your local workspace;
4. Create DockerFile according to the 3rd step;
5. Build Docker Image by the generated DockerFile, and upload it to Docker Hub [account mudongliang](https://hub.docker.com/u/mudongliang/);
7. Writing Vulnerability Analysis Document and upload it to [LinuxFlaw repo](https://github.com/mudongliang/LinuxFlaw);

All the information related to one vulnerability can be found in the corresponding folders in [LinuxFlaw repo](https://github.com/mudongliang/LinuxFlaw);

Note: Please keep name of all the folders / repos are the same with the one in LinuxFlaw. You can refer to [EDB-34164](https://github.com/mudongliang/LinuxFlaw/tree/master/EDB-34164)

References:
[1] [source-packages](https://github.com/mudongliang/source-packages)
[2] [LinuxFlaw](https://github.com/mudongliang/LinuxFlaw)
[3] [exploit-database](https://github.com/offensive-security/exploit-database/)
[4] [mudongliang](https://hub.docker.com/u/mudongliang/) 


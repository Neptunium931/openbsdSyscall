| NR | SYSCALL NAME | RAX | ARG0 (rdi) | ARG1 (rsi) | ARG2 (rdx) | ARG3 (rcx) | ARG4 (r8) | ARG5 (r9)
| --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- | --------------- |
|0|syscall|0x0|-|-|-|-|-|-|
|1|sys_exit|0x1|int rval|-|-|-|-|-|
|2|sys_fork|0x2|void|-|-|-|-|-|
|3|sys_read|0x3|int fd| void *buf| size_t nbyte|-|-|-|
|4|sys_write|0x4|int fd| const void *buf| size_t nbyte|-|-|-|
|5|sys_open|0x5|const char *path| int flags| ... mode_t mode|-|-|-|
|6|sys_close|0x6|int fd|-|-|-|-|-|
|7|sys_getentropy|0x7|void *buf| size_t nbyte|-|-|-|-|
|8|sys___tfork|0x8|const struct __tfork *param| size_t psize|-|-|-|-|
|9|sys_link|0x9|const char *path| const char *link|-|-|-|-|
|10|sys_unlink|0xa|const char *path|-|-|-|-|-|
|11|sys_wait4|0xb|pid_t pid| int *status| int options| struct rusage *rusage|-|-|
|12|sys_chdir|0xc|const char *path|-|-|-|-|-|
|13|sys_fchdir|0xd|int fd|-|-|-|-|-|
|14|sys_mknod|0xe|const char *path| mode_t mode| dev_t dev|-|-|-|
|15|sys_chmod|0xf|const char *path| mode_t mode|-|-|-|-|
|16|sys_chown|0x10|const char *path| uid_t uid| gid_t gid|-|-|-|
|17|sys_obreak|0x11|char *nsize|-|-|-|-|-|
|18|sys_getdtablecount|0x12|void|-|-|-|-|-|
|19|sys_getrusage|0x13|int who| struct rusage *rusage|-|-|-|-|
|20|sys_getpid|0x14|void|-|-|-|-|-|
|21|sys_mount|0x15|const char *type| const char *path| int flags| void *data|-|-|
|22|sys_unmount|0x16|const char *path| int flags|-|-|-|-|
|23|sys_setuid|0x17|uid_t uid|-|-|-|-|-|
|24|sys_getuid|0x18|void|-|-|-|-|-|
|25|sys_geteuid|0x19|void|-|-|-|-|-|
|26|sys_ptrace|0x1a|int req| pid_t pid| caddr_t addr| int data|-|-|
|26|ptrace|0x1a|-|-|-|-|-|-|
|27|sys_recvmsg|0x1b|int s| struct msghdr *msg| int flags|-|-|-|
|28|sys_sendmsg|0x1c|int s| const struct msghdr *msg| int flags|-|-|-|
|29|sys_recvfrom|0x1d|int s| void *buf| size_t len| int flags| struct sockaddr *from| socklen_t *fromlenaddr|
|30|sys_accept|0x1e|int s| struct sockaddr *name| socklen_t *anamelen|-|-|-|
|31|sys_getpeername|0x1f|int fdes| struct sockaddr *asa| socklen_t *alen|-|-|-|
|32|sys_getsockname|0x20|int fdes| struct sockaddr *asa| socklen_t *alen|-|-|-|
|33|sys_access|0x21|const char *path| int amode|-|-|-|-|
|34|sys_chflags|0x22|const char *path| u_int flags|-|-|-|-|
|35|sys_fchflags|0x23|int fd| u_int flags|-|-|-|-|
|36|sys_sync|0x24|void|-|-|-|-|-|
|37|msyscall|0x25|-|-|-|-|-|-|
|38|sys_stat|0x26|const char *path| struct stat *ub|-|-|-|-|
|39|sys_getppid|0x27|void|-|-|-|-|-|
|40|sys_lstat|0x28|const char *path| struct stat *ub|-|-|-|-|
|41|sys_dup|0x29|int fd|-|-|-|-|-|
|42|sys_fstatat|0x2a|int fd| const char *path| struct stat *buf| int flag|-|-|
|43|sys_getegid|0x2b|void|-|-|-|-|-|
|44|sys_profil|0x2c|caddr_t samples| size_t size| u_long offset| u_int scale|-|-|
|45|sys_ktrace|0x2d|const char *fname| int ops| int facs| pid_t pid|-|-|
|45|ktrace|0x2d|-|-|-|-|-|-|
|46|sys_sigaction|0x2e|int signum| const struct sigaction *nsa| struct sigaction *osa|-|-|-|
|47|sys_getgid|0x2f|void|-|-|-|-|-|
|48|sys_sigprocmask|0x30|int how| sigset_t mask|-|-|-|-|
|49|sys_mmap|0x31|void *addr| size_t len| int prot| int flags| int fd| off_t pos|
|50|sys_setlogin|0x32|const char *namebuf|-|-|-|-|-|
|51|sys_acct|0x33|const char *path|-|-|-|-|-|
|51|acct|0x33|-|-|-|-|-|-|
|52|sys_sigpending|0x34|void|-|-|-|-|-|
|53|sys_fstat|0x35|int fd| struct stat *sb|-|-|-|-|
|54|sys_ioctl|0x36|int fd| u_long com| ... void *data|-|-|-|
|55|sys_reboot|0x37|int opt|-|-|-|-|-|
|56|sys_revoke|0x38|const char *path|-|-|-|-|-|
|57|sys_symlink|0x39|const char *path| const char *link|-|-|-|-|
|58|sys_readlink|0x3a|const char *path| char *buf| size_t count|-|-|-|
|59|sys_execve|0x3b|const char *path| char * const *argp| char * const *envp|-|-|-|
|60|sys_umask|0x3c|mode_t newmask|-|-|-|-|-|
|61|sys_chroot|0x3d|const char *path|-|-|-|-|-|
|62|sys_getfsstat|0x3e|struct statfs *buf| size_t bufsize| int flags|-|-|-|
|63|sys_statfs|0x3f|const char *path| struct statfs *buf|-|-|-|-|
|64|sys_fstatfs|0x40|int fd| struct statfs *buf|-|-|-|-|
|65|sys_fhstatfs|0x41|const fhandle_t *fhp| struct statfs *buf|-|-|-|-|
|66|sys_vfork|0x42|void|-|-|-|-|-|
|67|sys_gettimeofday|0x43|struct timeval *tp| struct timezone *tzp|-|-|-|-|
|68|sys_settimeofday|0x44|const struct timeval *tv| const struct timezone *tzp|-|-|-|-|
|69|sys_setitimer|0x45|int which| const struct itimerval *itv| struct itimerval *oitv|-|-|-|
|70|sys_getitimer|0x46|int which| struct itimerval *itv|-|-|-|-|
|71|sys_select|0x47|int nd| fd_set *in| fd_set *ou| fd_set *ex| struct timeval *tv|-|
|72|sys_kevent|0x48|int fd| const struct kevent *changelist| int nchanges| struct kevent *eventlist| int nevents| const struct timespec *timeout|
|73|sys_munmap|0x49|void *addr| size_t len|-|-|-|-|
|74|sys_mprotect|0x4a|void *addr| size_t len| int prot|-|-|-|
|75|sys_madvise|0x4b|void *addr| size_t len| int behav|-|-|-|
|76|sys_utimes|0x4c|const char *path| const struct timeval *tptr|-|-|-|-|
|77|sys_futimes|0x4d|int fd| const struct timeval *tptr|-|-|-|-|
|78|sys_mquery|0x4e|void *addr| size_t len| int prot| int flags| int fd| off_t pos|
|79|sys_getgroups|0x4f|int gidsetsize| gid_t *gidset|-|-|-|-|
|80|sys_setgroups|0x50|int gidsetsize| const gid_t *gidset|-|-|-|-|
|81|sys_getpgrp|0x51|void|-|-|-|-|-|
|82|sys_setpgid|0x52|pid_t pid| pid_t pgid|-|-|-|-|
|83|sys_futex|0x53|uint32_t *f| int op| int val| const struct timespec *timeout| uint32_t *g|-|
|84|sys_utimensat|0x54|int fd| const char *path| const struct timespec *times| int flag|-|-|
|85|sys_futimens|0x55|int fd| const struct timespec *times|-|-|-|-|
|86|sys_kbind|0x56|const struct __kbind *param| size_t psize| int64_t proc_cookie|-|-|-|
|87|sys_clock_gettime|0x57|clockid_t clock_id| struct timespec *tp|-|-|-|-|
|88|sys_clock_settime|0x58|clockid_t clock_id| const struct timespec *tp|-|-|-|-|
|89|sys_clock_getres|0x59|clockid_t clock_id| struct timespec *tp|-|-|-|-|
|90|sys_dup2|0x5a|int from| int to|-|-|-|-|
|91|sys_nanosleep|0x5b|const struct timespec *rqtp| struct timespec *rmtp|-|-|-|-|
|92|sys_fcntl|0x5c|int fd| int cmd| ... void *arg|-|-|-|
|93|sys_accept4|0x5d|int s| struct sockaddr *name| socklen_t *anamelen| int flags|-|-|
|94|sys___thrsleep|0x5e|const volatile void *ident| clockid_t clock_id| const struct timespec *tp| void *lock| const int *abort|-|
|95|sys_fsync|0x5f|int fd|-|-|-|-|-|
|96|sys_setpriority|0x60|int which| id_t who| int prio|-|-|-|
|97|sys_socket|0x61|int domain| int type| int protocol|-|-|-|
|98|sys_connect|0x62|int s| const struct sockaddr *name| socklen_t namelen|-|-|-|
|99|sys_getdents|0x63|int fd| void *buf| size_t buflen|-|-|-|
|100|sys_getpriority|0x64|int which| id_t who|-|-|-|-|
|101|sys_pipe2|0x65|int *fdp| int flags|-|-|-|-|
|102|sys_dup3|0x66|int from| int to| int flags|-|-|-|
|103|sys_sigreturn|0x67|struct sigcontext *sigcntxp|-|-|-|-|-|
|104|sys_bind|0x68|int s| const struct sockaddr *name| socklen_t namelen|-|-|-|
|105|sys_setsockopt|0x69|int s| int level| int name| const void *val| socklen_t valsize|-|
|106|sys_listen|0x6a|int s| int backlog|-|-|-|-|
|107|sys_chflagsat|0x6b|int fd| const char *path| u_int flags| int atflags|-|-|
|108|sys_pledge|0x6c|const char *promises| const char *execpromises|-|-|-|-|
|109|sys_ppoll|0x6d|struct pollfd *fds| u_int nfds| const struct timespec *ts| const sigset_t *mask|-|-|
|110|sys_pselect|0x6e|int nd| fd_set *in| fd_set *ou| fd_set *ex| const struct timespec *ts| const sigset_t *mask|
|111|sys_sigsuspend|0x6f|int mask|-|-|-|-|-|
|112|sys_sendsyslog|0x70|const char *buf| size_t nbyte| int flags|-|-|-|
|113|fktrace|0x71|-|-|-|-|-|-|
|114|sys_unveil|0x72|const char *path| const char *permissions|-|-|-|-|
|115|sys___realpath|0x73|const char *pathname| char *resolved|-|-|-|-|
|116|sys_recvmmsg|0x74|int s| struct mmsghdr *mmsg| unsigned int vlen| int flags| struct timespec *timeout|-|
|117|sys_sendmmsg|0x75|int s| struct mmsghdr *mmsg| unsigned int vlen| int flags|-|-|
|118|sys_getsockopt|0x76|int s| int level| int name| void *val| socklen_t *avalsize|-|
|119|sys_thrkill|0x77|pid_t tid| int signum| void *tcb|-|-|-|
|120|sys_readv|0x78|int fd| const struct iovec *iovp| int iovcnt|-|-|-|
|121|sys_writev|0x79|int fd| const struct iovec *iovp| int iovcnt|-|-|-|
|122|sys_kill|0x7a|int pid| int signum|-|-|-|-|
|123|sys_fchown|0x7b|int fd| uid_t uid| gid_t gid|-|-|-|
|124|sys_fchmod|0x7c|int fd| mode_t mode|-|-|-|-|
|125|orecvfrom|0x7d|-|-|-|-|-|-|
|126|sys_setreuid|0x7e|uid_t ruid| uid_t euid|-|-|-|-|
|127|sys_setregid|0x7f|gid_t rgid| gid_t egid|-|-|-|-|
|128|sys_rename|0x80|const char *from| const char *to|-|-|-|-|
|129|otruncate|0x81|-|-|-|-|-|-|
|130|oftruncate|0x82|-|-|-|-|-|-|
|131|sys_flock|0x83|int fd| int how|-|-|-|-|
|132|sys_mkfifo|0x84|const char *path| mode_t mode|-|-|-|-|
|133|sys_sendto|0x85|int s| const void *buf| size_t len| int flags| const struct sockaddr *to| socklen_t tolen|
|134|sys_shutdown|0x86|int s| int how|-|-|-|-|
|135|sys_socketpair|0x87|int domain| int type| int protocol| int *rsv|-|-|
|136|sys_mkdir|0x88|const char *path| mode_t mode|-|-|-|-|
|137|sys_rmdir|0x89|const char *path|-|-|-|-|-|
|138|t32_utimes|0x8a|-|-|-|-|-|-|
|139|sigreturn|0x8b|-|-|-|-|-|-|
|140|sys_adjtime|0x8c|const struct timeval *delta| struct timeval *olddelta|-|-|-|-|
|141|sys_getlogin_r|0x8d|char *namebuf| size_t namelen|-|-|-|-|
|142|sys_getthrname|0x8e|pid_t tid| char *name| size_t len|-|-|-|
|143|sys_setthrname|0x8f|pid_t tid| const char *name|-|-|-|-|
|144|ogetrlimit|0x90|-|-|-|-|-|-|
|145|osetrlimit|0x91|-|-|-|-|-|-|
|146|pinsyscall|0x92|-|-|-|-|-|-|
|147|sys_setsid|0x93|void|-|-|-|-|-|
|148|sys_quotactl|0x94|const char *path| int cmd| int uid| char *arg|-|-|
|149|oquota|0x95|-|-|-|-|-|-|
|150|sys_ypconnect|0x96|int type|-|-|-|-|-|
|151|UNIMPL|0x97|-|-|-|-|-|-|
|152|UNIMPL|0x98|-|-|-|-|-|-|
|153|UNIMPL|0x99|-|-|-|-|-|-|
|154|UNIMPL|0x9a|-|-|-|-|-|-|
|155|sys_nfssvc|0x9b|int flag| void *argp|-|-|-|-|
|155|UNIMPL|0x9b|-|-|-|-|-|-|
|156|ogetdirentries|0x9c|-|-|-|-|-|-|
|157|statfs25|0x9d|-|-|-|-|-|-|
|158|sys_pinsyscalls|0x9e|void *base| size_t len| u_int *pins| int npins|-|-|
|159|sys_mimmutable|0x9f|void *addr| size_t len|-|-|-|-|
|160|sys_waitid|0xa0|int idtype| id_t id| siginfo_t *info| int options|-|-|
|161|sys_getfh|0xa1|const char *fname| fhandle_t *fhp|-|-|-|-|
|162|ogetdomainname|0xa2|-|-|-|-|-|-|
|163|osetdomainname|0xa3|-|-|-|-|-|-|
|164|sys___tmpfd|0xa4|int flags|-|-|-|-|-|
|165|sys_sysarch|0xa5|int op| void *parms|-|-|-|-|
|166|sys_lseek|0xa6|int fd| off_t offset| int whence|-|-|-|
|167|sys_truncate|0xa7|const char *path| off_t length|-|-|-|-|
|168|sys_ftruncate|0xa8|int fd| off_t length|-|-|-|-|
|169|sys_pread|0xa9|int fd| void *buf| size_t nbyte| off_t offset|-|-|
|170|sys_pwrite|0xaa|int fd| const void *buf| size_t nbyte| off_t offset|-|-|
|171|sys_preadv|0xab|int fd| const struct iovec *iovp| int iovcnt| off_t offset|-|-|
|172|sys_pwritev|0xac|int fd| const struct iovec *iovp| int iovcnt| off_t offset|-|-|
|173|pad_pread|0xad|-|-|-|-|-|-|
|174|pad_pwrite|0xae|-|-|-|-|-|-|
|175|ntp_gettime|0xaf|-|-|-|-|-|-|
|176|ntp_adjtime|0xb0|-|-|-|-|-|-|
|177|UNIMPL|0xb1|-|-|-|-|-|-|
|178|UNIMPL|0xb2|-|-|-|-|-|-|
|179|UNIMPL|0xb3|-|-|-|-|-|-|
|180|UNIMPL|0xb4|-|-|-|-|-|-|
|181|sys_setgid|0xb5|gid_t gid|-|-|-|-|-|
|182|sys_setegid|0xb6|gid_t egid|-|-|-|-|-|
|183|sys_seteuid|0xb7|uid_t euid|-|-|-|-|-|
|184|lfs_bmapv|0xb8|-|-|-|-|-|-|
|185|lfs_markv|0xb9|-|-|-|-|-|-|
|186|lfs_segclean|0xba|-|-|-|-|-|-|
|187|lfs_segwait|0xbb|-|-|-|-|-|-|
|188|stat35|0xbc|-|-|-|-|-|-|
|189|fstat35|0xbd|-|-|-|-|-|-|
|190|sys_pathconfat|0xbe|int fd| const char *path| int name| int flag|-|-|
|191|sys_pathconf|0xbf|const char *path| int name|-|-|-|-|
|192|sys_fpathconf|0xc0|int fd| int name|-|-|-|-|
|193|sys_swapctl|0xc1|int cmd| const void *arg| int misc|-|-|-|
|194|sys_getrlimit|0xc2|int which| struct rlimit *rlp|-|-|-|-|
|195|sys_setrlimit|0xc3|int which| const struct rlimit *rlp|-|-|-|-|
|196|ogetdirentries48|0xc4|-|-|-|-|-|-|
|197|pad_mmap|0xc5|-|-|-|-|-|-|
|198|__syscall|0xc6|-|-|-|-|-|-|
|199|pad_lseek|0xc7|-|-|-|-|-|-|
|200|pad_truncate|0xc8|-|-|-|-|-|-|
|201|pad_ftruncate|0xc9|-|-|-|-|-|-|
|202|sys_sysctl|0xca|const int *name| u_int namelen| void *old| size_t *oldlenp| void *new| size_t newlen|
|203|sys_mlock|0xcb|const void *addr| size_t len|-|-|-|-|
|204|sys_munlock|0xcc|const void *addr| size_t len|-|-|-|-|
|205|sys_undelete|0xcd|-|-|-|-|-|-|
|206|t32_futimes|0xce|-|-|-|-|-|-|
|207|sys_getpgid|0xcf|pid_t pid|-|-|-|-|-|
|208|nnpfspioctl|0xd0|-|-|-|-|-|-|
|209|sys_utrace|0xd1|const char *label| const void *addr| size_t len|-|-|-|
|210|UNIMPL|0xd2|-|-|-|-|-|-|
|211|UNIMPL|0xd3|-|-|-|-|-|-|
|212|UNIMPL|0xd4|-|-|-|-|-|-|
|213|UNIMPL|0xd5|-|-|-|-|-|-|
|214|UNIMPL|0xd6|-|-|-|-|-|-|
|215|UNIMPL|0xd7|-|-|-|-|-|-|
|216|UNIMPL|0xd8|-|-|-|-|-|-|
|217|UNIMPL|0xd9|-|-|-|-|-|-|
|218|UNIMPL|0xda|-|-|-|-|-|-|
|219|UNIMPL|0xdb|-|-|-|-|-|-|
|220|UNIMPL|0xdc|-|-|-|-|-|-|
|221|sys_semget|0xdd|key_t key| int nsems| int semflg|-|-|-|
|220|semctl|0xdc|-|-|-|-|-|-|
|221|semget|0xdd|-|-|-|-|-|-|
|222|semop35|0xde|-|-|-|-|-|-|
|223|semconfig35|0xdf|-|-|-|-|-|-|
|224|UNIMPL|0xe0|-|-|-|-|-|-|
|225|sys_msgget|0xe1|key_t key| int msgflg|-|-|-|-|
|226|sys_msgsnd|0xe2|int msqid| const void *msgp| size_t msgsz| int msgflg|-|-|
|227|sys_msgrcv|0xe3|int msqid| void *msgp| size_t msgsz| long msgtyp| int msgflg|-|
|224|msgctl|0xe0|-|-|-|-|-|-|
|225|msgget|0xe1|-|-|-|-|-|-|
|226|msgsnd|0xe2|-|-|-|-|-|-|
|227|msgrcv|0xe3|-|-|-|-|-|-|
|228|sys_shmat|0xe4|int shmid| const void *shmaddr| int shmflg|-|-|-|
|229|UNIMPL|0xe5|-|-|-|-|-|-|
|230|sys_shmdt|0xe6|const void *shmaddr|-|-|-|-|-|
|228|shmat|0xe4|-|-|-|-|-|-|
|229|shmctl|0xe5|-|-|-|-|-|-|
|230|shmdt|0xe6|-|-|-|-|-|-|
|231|shmget35|0xe7|-|-|-|-|-|-|
|232|t32_clock_gettime|0xe8|-|-|-|-|-|-|
|233|t32_clock_settime|0xe9|-|-|-|-|-|-|
|234|t32_clock_getres|0xea|-|-|-|-|-|-|
|235|timer_create|0xeb|-|-|-|-|-|-|
|236|timer_delete|0xec|-|-|-|-|-|-|
|237|timer_settime|0xed|-|-|-|-|-|-|
|238|timer_gettime|0xee|-|-|-|-|-|-|
|239|timer_getoverrun|0xef|-|-|-|-|-|-|
|240|t32_nanosleep|0xf0|-|-|-|-|-|-|
|241|UNIMPL|0xf1|-|-|-|-|-|-|
|242|UNIMPL|0xf2|-|-|-|-|-|-|
|243|UNIMPL|0xf3|-|-|-|-|-|-|
|244|UNIMPL|0xf4|-|-|-|-|-|-|
|245|UNIMPL|0xf5|-|-|-|-|-|-|
|246|UNIMPL|0xf6|-|-|-|-|-|-|
|247|UNIMPL|0xf7|-|-|-|-|-|-|
|248|UNIMPL|0xf8|-|-|-|-|-|-|
|249|UNIMPL|0xf9|-|-|-|-|-|-|
|250|sys_minherit|0xfa|void *addr| size_t len| int inherit|-|-|-|
|251|rfork|0xfb|-|-|-|-|-|-|
|252|sys_poll|0xfc|struct pollfd *fds| u_int nfds| int timeout|-|-|-|
|253|sys_issetugid|0xfd|void|-|-|-|-|-|
|254|sys_lchown|0xfe|const char *path| uid_t uid| gid_t gid|-|-|-|
|255|sys_getsid|0xff|pid_t pid|-|-|-|-|-|
|256|sys_msync|0x100|void *addr| size_t len| int flags|-|-|-|
|257|semctl35|0x101|-|-|-|-|-|-|
|258|shmctl35|0x102|-|-|-|-|-|-|
|259|msgctl35|0x103|-|-|-|-|-|-|
|260|UNIMPL|0x104|-|-|-|-|-|-|
|261|UNIMPL|0x105|-|-|-|-|-|-|
|262|UNIMPL|0x106|-|-|-|-|-|-|
|263|sys_pipe|0x107|int *fdp|-|-|-|-|-|
|264|sys_fhopen|0x108|const fhandle_t *fhp| int flags|-|-|-|-|
|265|UNIMPL|0x109|-|-|-|-|-|-|
|266|UNIMPL|0x10a|-|-|-|-|-|-|
|267|pad_preadv|0x10b|-|-|-|-|-|-|
|268|pad_pwritev|0x10c|-|-|-|-|-|-|
|269|sys_kqueue|0x10d|void|-|-|-|-|-|
|270|sys_kqueue1|0x10e|int flags|-|-|-|-|-|
|271|sys_mlockall|0x10f|int flags|-|-|-|-|-|
|272|sys_munlockall|0x110|void|-|-|-|-|-|
|273|sys_getpeereid|0x111|-|-|-|-|-|-|
|274|sys_extattrctl|0x112|-|-|-|-|-|-|
|275|sys_extattr_set_file|0x113|-|-|-|-|-|-|
|276|sys_extattr_get_file|0x114|-|-|-|-|-|-|
|277|sys_extattr_delete_file|0x115|-|-|-|-|-|-|
|278|sys_extattr_set_fd|0x116|-|-|-|-|-|-|
|279|sys_extattr_get_fd|0x117|-|-|-|-|-|-|
|280|sys_extattr_delete_fd|0x118|-|-|-|-|-|-|
|281|sys_getresuid|0x119|uid_t *ruid| uid_t *euid| uid_t *suid|-|-|-|
|282|sys_setresuid|0x11a|uid_t ruid| uid_t euid| uid_t suid|-|-|-|
|283|sys_getresgid|0x11b|gid_t *rgid| gid_t *egid| gid_t *sgid|-|-|-|
|284|sys_setresgid|0x11c|gid_t rgid| gid_t egid| gid_t sgid|-|-|-|
|285|sys_omquery|0x11d|-|-|-|-|-|-|
|286|pad_mquery|0x11e|-|-|-|-|-|-|
|287|sys_closefrom|0x11f|int fd|-|-|-|-|-|
|288|sys_sigaltstack|0x120|const struct sigaltstack *nss| struct sigaltstack *oss|-|-|-|-|
|289|sys_shmget|0x121|key_t key| size_t size| int shmflg|-|-|-|
|289|shmget|0x121|-|-|-|-|-|-|
|290|sys_semop|0x122|int semid| struct sembuf *sops| size_t nsops|-|-|-|
|290|semop|0x122|-|-|-|-|-|-|
|291|t32_stat|0x123|-|-|-|-|-|-|
|292|t32_fstat|0x124|-|-|-|-|-|-|
|293|t32_lstat|0x125|-|-|-|-|-|-|
|294|sys_fhstat|0x126|const fhandle_t *fhp| struct stat *sb|-|-|-|-|
|295|sys___semctl|0x127|int semid| int semnum| int cmd| union semun *arg|-|-|
|295|UNIMPL|0x127|-|-|-|-|-|-|
|296|sys_shmctl|0x128|int shmid| int cmd| struct shmid_ds *buf|-|-|-|
|296|UNIMPL|0x128|-|-|-|-|-|-|
|297|sys_msgctl|0x129|int msqid| int cmd| struct msqid_ds *buf|-|-|-|
|297|UNIMPL|0x129|-|-|-|-|-|-|
|298|sys_sched_yield|0x12a|void|-|-|-|-|-|
|299|sys_getthrid|0x12b|void|-|-|-|-|-|
|300|t32___thrsleep|0x12c|-|-|-|-|-|-|
|301|sys___thrwakeup|0x12d|const volatile void *ident| int n|-|-|-|-|
|302|sys___threxit|0x12e|pid_t *notdead|-|-|-|-|-|
|303|sys___thrsigdivert|0x12f|sigset_t sigmask| siginfo_t *info| const struct timespec *timeout|-|-|-|
|304|sys___getcwd|0x130|char *buf| size_t len|-|-|-|-|
|305|sys_adjfreq|0x131|const int64_t *freq| int64_t *oldfreq|-|-|-|-|
|306|getfsstat53|0x132|-|-|-|-|-|-|
|307|statfs53|0x133|-|-|-|-|-|-|
|308|fstatfs53|0x134|-|-|-|-|-|-|
|309|fhstatfs53|0x135|-|-|-|-|-|-|
|310|sys_setrtable|0x136|int rtableid|-|-|-|-|-|
|311|sys_getrtable|0x137|void|-|-|-|-|-|
|312|t32_getdirentries|0x138|-|-|-|-|-|-|
|313|sys_faccessat|0x139|int fd| const char *path| int amode| int flag|-|-|
|314|sys_fchmodat|0x13a|int fd| const char *path| mode_t mode| int flag|-|-|
|315|sys_fchownat|0x13b|int fd| const char *path| uid_t uid| gid_t gid| int flag|-|
|316|t32_fstatat|0x13c|-|-|-|-|-|-|
|317|sys_linkat|0x13d|int fd1| const char *path1| int fd2| const char *path2| int flag|-|
|318|sys_mkdirat|0x13e|int fd| const char *path| mode_t mode|-|-|-|
|319|sys_mkfifoat|0x13f|int fd| const char *path| mode_t mode|-|-|-|
|320|sys_mknodat|0x140|int fd| const char *path| mode_t mode| dev_t dev|-|-|
|321|sys_openat|0x141|int fd| const char *path| int flags| ... mode_t mode|-|-|
|322|sys_readlinkat|0x142|int fd| const char *path| char *buf| size_t count|-|-|
|323|sys_renameat|0x143|int fromfd| const char *from| int tofd| const char *to|-|-|
|324|sys_symlinkat|0x144|const char *path| int fd| const char *link|-|-|-|
|325|sys_unlinkat|0x145|int fd| const char *path| int flag|-|-|-|
|326|t32_utimensat|0x146|-|-|-|-|-|-|
|327|t32_futimens|0x147|-|-|-|-|-|-|
|328|__tfork51|0x148|-|-|-|-|-|-|
|329|sys___set_tcb|0x149|void *tcb|-|-|-|-|-|
|330|sys___get_tcb|0x14a|void|-|-|-|-|-|

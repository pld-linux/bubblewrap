Summary:	bubblewrap - container setup utility
Summary(pl.UTF-8):	bubblewrap - narzędzie do tworzenia kontenerów
Name:		bubblewrap
Version:	0.1.5
Release:	2
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://github.com/projectatomic/bubblewrap/releases
Source0:	https://github.com/projectatomic/bubblewrap/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	12cb7c19749c70f937a9ef2372215881
URL:		https://github.com/projectatomic/bubblewrap
BuildRequires:	libcap-devel
BuildRequires:	libselinux-devel >= 2.1.9
BuildRequires:	libxslt-progs
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libselinux >= 2.1.9
Requires:	uname(release) >= 3.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bwrap is a privileged helper for container setup.

It works by creating a new, completely empty, filesystem namespace
where the root is on a tmpfs that is invisible from the host, and
which will be automatically cleaned up when the last process exists.
You can then use commandline options to construct the root filesystem
and process environment for the command to run in the namespace.

%description -l pl.UTF-8
bwrap to uprzywilejowany program pomocniczy do tworzenia kontenerów.

Działa tworząc nową, całkowicie pustą przestrzeń nazw systemu plików,
gdzie katalog główny jest na tmpfs-ie całkowicie niewidocznym z hosta,
czyszczonym automatycznie po zakończeniu ostatniego procesu. Do
tworzenia głównego systemu plików i środowiska procesów do
uruchamiania poleceń w środowisku można używać opcji linii poleceń.

%package -n bash-completion-bubblewrap
Summary:	Bash completion for bwrap command
Summary(pl.UTF-8):	Bashowe dopełnianie parametrów polecenia bwrap
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	bash-completion >= 2.0

%description -n bash-completion-bubblewrap
Bash completion for bwrap command.

%description -n bash-completion-bubblewrap -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia bwrap.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/bwrap
%{_mandir}/man1/bwrap.1*

%files -n bash-completion-bubblewrap
%defattr(644,root,root,755)
%{bash_compdir}/bwrap

Summary:	bubblewrap - container setup utility
Summary(pl.UTF-8):	bubblewrap - narzędzie do tworzenia kontenerów
Name:		bubblewrap
Version:	0.10.0
Release:	1
License:	LGPL v2+
Group:		Applications/System
#Source0Download: https://github.com/containers/bubblewrap/releases
Source0:	https://github.com/containers/bubblewrap/releases/download/v%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	85f144f6c2c28c112abbcf98bedf6137
URL:		https://github.com/containers/bubblewrap
BuildRequires:	docbook-style-xsl-nons
BuildRequires:	libcap-devel
BuildRequires:	libselinux-devel >= 2.3
BuildRequires:	libxslt-progs
BuildRequires:	meson >= 0.49.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	libselinux >= 2.3
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
Requires:	bash-completion >= 1:2.0
BuildArch:	noarch

%description -n bash-completion-bubblewrap
Bash completion for bwrap command.

%description -n bash-completion-bubblewrap -l pl.UTF-8
Bashowe dopełnianie parametrów polecenia bwrap.

%package -n zsh-completion-bubblewrap
Summary:	ZSH completion for bwrap command
Summary(pl.UTF-8):	Dopełnianie parametrów polecenia bwrap dla ZSH
Group:		Applications/Shells
Requires:	%{name} = %{version}-%{release}
Requires:	zsh-completions
BuildArch:	noarch

%description -n zsh-completion-bubblewrap
ZSH completion for bwrap command.

%description -n zsh-completion-bubblewrap -l pl.UTF-8
Dopełnianie parametrów polecenia bwrap dla ZSH.

%prep
%setup -q

%build
%meson build \
	-Dbash_completion_dir=%{bash_compdir} \
	-Dzsh_completion_dir=%{zsh_compdir}

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/bwrap
%{_mandir}/man1/bwrap.1*

%files -n bash-completion-bubblewrap
%defattr(644,root,root,755)
%{bash_compdir}/bwrap

%files -n zsh-completion-bubblewrap
%defattr(644,root,root,755)
%{zsh_compdir}/_bwrap

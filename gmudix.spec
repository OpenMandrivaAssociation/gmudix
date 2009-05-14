%define	name	gmudix
%define	version	1.0
%define	release 4	
%define	Summary	GMudix GTK mud client

Name:		%{name} 
Summary:	%{Summary}
Version:	%{version} 
Release:	%mkrel %{release} 
Source0:	%{name}-%{version}.tar.bz2
Patch0: 	%{name}-fix-str-fmt.diff
Patch1:     %{name}-fix-linking-problem.diff
URL:		http://dw.nl.eu.org/mudix.html
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	LGPL
BuildRequires:	gtk+2-devel

%description
gMudix is a GTK mud client that supports ANSI colours.
Some of the features are aliases, macros, paths,
tab completion, timers and triggers.

%prep
%setup -q
%patch0 -p1 -b .str-fmt
%patch1 -p0

%build
aclocal
autoconf
automake -a
%configure	--bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}
Icon=other_amusement
Categories=Game;RolePlaying;
Name=gMudix
Comment=%{Summary}
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc TODO README AUTHORS ChangeLog
%{_gamesbindir}/%{name}
%{_datadir}/applications/mandriva-%{name}.desktop


%define	name	gmudix
%define	version	1.0
%define	release	3
%define	Summary	GMudix GTK mud client

Name:		%{name} 
Summary:	%{Summary}
Version:	%{version} 
Release:	%mkrel %{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://dw.nl.eu.org/mudix.html
Group:		Games/Other
License:	LGPL
BuildRequires:	gtk+2-devel

%description
gMudix is a GTK mud client that supports ANSI colours.
Some of the features are aliases, macros, paths,
tab completion, timers and triggers.

%prep
%setup -q

%build
%configure	--bindir=%{_gamesbindir}
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall_std}

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
icon="other_amusement.png" needs="X11" section="More applications/Games/Other" \
title="gMudix" \
longtitle="%{Summary}"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc TODO README AUTHORS ChangeLog
%{_gamesbindir}/%{name}
%{_menudir}/%{name}


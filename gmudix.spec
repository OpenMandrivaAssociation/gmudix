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
URL:		https://dw.nl.eu.org/mudix.html
Group:		Games/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPLv2+
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



%changelog
* Thu May 14 2009 Samuel Verschelde <stormi@mandriva.org> 1.0-4mdv2010.0
+ Revision: 375658
- fix Licence
- fix menu category
- fix str fmt

  + Michael Scherer <misc@mandriva.org>
    - fix underlinking issues

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0-3mdv2008.1
+ Revision: 131647
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request
- import gmudix


* Fri Oct 07 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-3mdk
- rebuild for new cairo

* Mon Aug 08 2005 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.0-2mdk
- rebuild
- %%mkrel

* Wed Jun 23 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0-1mdk
- spec fixes
- from Eskild Hustvedt <eskild@mandrakehelp.com>:
	o Initial Mandrakelinux package

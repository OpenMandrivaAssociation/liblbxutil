%define name		liblbxutil
%define version		1.1.0
%define release		%mkrel 5

%define libname 	%mklibname lbxutil 1
%define develname	%mklibname lbxutil -d
%define staticname	%mklibname lbxutil -d -s

Name: %{name}
Summary: LBX Utility library
Version: %{version}
Release: %{release}
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: zlib-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
LBX Utility library.

#-----------------------------------------------------------
%package -n %{libname}
Summary: LBX Utilities
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libname}
LBX Utility library.

#-----------------------------------------------------------

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libname} = %{version}
Provides: %{name}-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0
Conflicts: %{_lib}xext-devel < 1:1.1.1-2
Obsoletes: %{mklibname lbxutil 1 -d}

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_includedir}/X11/extensions/*.h
%{_libdir}/liblbxutil.so
%{_libdir}/pkgconfig/lbxutil.pc

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: %{name}-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0
Obsoletes: %{mklibname lbxutil 1 -d -s}

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/liblbxutil.a

#-----------------------------------------------------------

%prep
%setup -q -n liblbxutil-%{version}

%build
%define _disable_ld_no_undefined 1
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblbxutil.so.1
%{_libdir}/liblbxutil.so.1.0.0


%changelog
* Wed Apr 13 2011 Funda Wang <fwang@mandriva.org> 1.1.0-4mdv2011.0
+ Revision: 653140
- tweak conflicts

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3mdv2011.0
+ Revision: 602567
- rebuild

* Mon Jan 04 2010 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2010.1
+ Revision: 486085
- add conflicts with older release of xext

* Sun Jan 03 2010 Funda Wang <fwang@mandriva.org> 1.1.0-1mdv2010.1
+ Revision: 486031
- New version 1.1.0

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.1-8mdv2010.0
+ Revision: 425591
- rebuild

* Sun Jul 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-7mdv2009.0
+ Revision: 232153
- use _disable_ld_no_undefined due to build problems

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert build requires.

* Wed Jan 16 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.1-5mdv2008.1
+ Revision: 153796
- Update BuildRequires and resubmit package.

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-4mdv2008.1
+ Revision: 150702
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Jul 25 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.1-3mdv2008.0
+ Revision: 55101
- rebuild for 2008
- new devel policy
- spec clean


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Thu May 25 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-25 20:17:57 (31598)
- X11R7.1

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:35:26 (27467)
- fix my fix

* Tue May 16 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-16 23:34:58 (27466)
- fix description

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 19:54:51 (26912)
- fixed more dependencies

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository


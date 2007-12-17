%define name	liblbxutil
%define version	1.0.1
%define release	%mkrel 3

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
Obsoletes: %{mklibname lbxutil 1 -d}

%description -n %{develname}
Development files for %{name}

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/liblbxutil.so
%{_libdir}/liblbxutil.la
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
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/liblbxutil.so.1
%{_libdir}/liblbxutil.so.1.0.0

%define liblbxutil %mklibname lbxutil 1
Name: liblbxutil
Summary: LBX Utility library
Version: 1.0.1
Release: %mkrel 2
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/liblbxutil-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: zlib-devel
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
LBX Utility library.

#-----------------------------------------------------------
%package -n %{liblbxutil}
Summary: LBX Utilities
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{liblbxutil}
LBX Utility library.

#-----------------------------------------------------------

%package -n %{liblbxutil}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{liblbxutil} = %{version}
Provides: liblbxutil-devel = %{version}-%{release}
Conflicts: libxorg-x11-devel < 7.0

%description -n %{liblbxutil}-devel
Development files for %{name}

%files -n %{liblbxutil}-devel
%defattr(-,root,root)
%{_libdir}/liblbxutil.so
%{_libdir}/liblbxutil.la
%{_libdir}/pkgconfig/lbxutil.pc

#-----------------------------------------------------------

%package -n %{liblbxutil}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{liblbxutil}-devel = %{version}
Provides: liblbxutil-static-devel = %{version}-%{release}
Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{liblbxutil}-static-devel
Static development files for %{name}

%files -n %{liblbxutil}-static-devel
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

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{liblbxutil}
%defattr(-,root,root)
%{_libdir}/liblbxutil.so.1
%{_libdir}/liblbxutil.so.1.0.0



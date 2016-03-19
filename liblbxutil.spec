%define major	1
%define libname	%mklibname lbxutil %{major}
%define devname	%mklibname lbxutil -d

Summary:	LBX Utility library
Name:		liblbxutil
Version:	1.1.0
Release:	16
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/%{name}-%{version}.tar.bz2
Patch0:		aarch64.patch

BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(zlib)

%description
LBX Utility library.

%package -n %{libname}
Summary:	LBX Utilities
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
LBX Utility library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}

%prep
%setup -q
%apply_patches

%build
%define _disable_ld_no_undefined 1
%configure2_5x \
	--disable-static
%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/liblbxutil.so.%{major}*

%files -n %{devname}
%{_includedir}/X11/extensions/*.h
%{_libdir}/liblbxutil.so
%{_libdir}/pkgconfig/lbxutil.pc


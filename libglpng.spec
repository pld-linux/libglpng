Summary:	PNG loader library for OpenGL
Summary(pl.UTF-8):	Biblioteka ładująca PNG dla OpenGL
Name:		libglpng
Version:	1.45
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://www.wyatt100.freeserve.co.uk/glpng.zip
# Source0-md5:	bed59efb699a51e6de7434580df41395
Patch0:		%{name}-debian.patch
Patch1:		%{name}-Makefile.patch
URL:		http://www.fachschaften.neuphilologie.uni-tuebingen.de/doc/libglpng/glpng.html
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1

%description
This is a library for OpenGL to load PNG graphics files as an OpenGL
texture as easily as possible.

%description -l pl.UTF-8
To jest biblioteka dla OpenGL pozwalająca ładować grafikę PNG jako
tekstury OpenGL.

%package devel
Summary:	Libraries, includes, etc to develop libglpng applications
Summary(pl.UTF-8):	Pliki developerskie libglpng
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	OpenGL-devel

%description devel
Libraries, includes, etc to develop libglpng applications.

%description devel -l pl.UTF-8
Pliki developerskie libglpng.

%package static
Summary:	Static libglpng library
Summary(pl.UTF-8):	Biblioteka statyczna libglpng
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libglpng library.

%description static -l pl.UTF-8
Biblioteka statyczna libglpng.

%prep
%setup -q -c
%patch0 -p1
%patch1 -p1

%build
%{__make} \
	CC="%{__cc}" \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR=%{_libdir} \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

rm -f Example/*.exe

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.htm
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc Example/*
%{_includedir}/GL/*.h
%attr(755,root,root) %{_libdir}/lib*.so

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

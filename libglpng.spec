Summary:	PNG loader library for OpenGL
Summary(pl):	Biblioteka ³aduj±ca PNG dla OpenGL
Name:		libglpng
Version:	1.45
Release:	1
License:	BSD
Group:		X11/Libraries
Source0:	http://www.wyatt100.freeserve.co.uk/glpng.zip
Patch0:		%{name}-debian.patch
URL:		http://www.fachschaften.neuphilologie.uni-tuebingen.de/doc/libglpng/glpng.html
BuildRequires:	OpenGL-devel
BuildRequires:	libpng-devel
BuildRequires:	unzip
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6

%description
This is a library for OpenGL to load PNG graphics files as an OpenGL
texture as easily as possible.

%description -l pl
To jest biblioteka dla OpenGL pozwalaj±ca ³adowaæ grafikê PNG jako
tekstury OpenGL.

%package devel
Summary:	Libraries, includes, etc to develop libglpng applications
Summary(pl):	Pliki developerskie libglpng
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	OpenGL-devel

%description devel
Libraries, includes, etc to develop libglpng applications.

%description devel -l pl
Pliki developerskie libglpng.

%package static
Summary:	Static libglpng library
Summary(pl):	Biblioteka statyczna libglpng
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libglpng library.

%description static -l pl
Biblioteka statyczna libglpng.

%prep
%setup -q -c -n %{name}-%{version}
%patch0 -p1

%build
%{__make} CC="%{__cc}" OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT%{_prefix}

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

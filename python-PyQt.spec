# TODO:
#   - Fix linking with qscintilla. Still qtext module does not build.
%include	/usr/lib/rpm/macros.python
%define		module	PyQt
Summary:	Python bindings for the Qt toolkit
Summary(pl):	Dowi±zania do toolkitu Qt dla Pythona
Name:		python-%{module}
Version:	3.7
Release:	1.1
License:	GPL
Group:		Libraries/Python
Source0:	http://www.river-bank.demon.co.uk/download/PyQt/PyQt-x11-gpl-%{version}.tar.gz
# Source0-md5:	f782882fc770e6b1dc97054fe73fafee
# Source0:	http://www.river-bank.demon.co.uk/download/snapshots/PyQt/PyQt-x11-gpl-snapshot-%{snap}.tar.gz
URL:		http://www.riverbankcomputing.co.uk/pyqt/index.php
BuildRequires:	python-devel >= 2.2.2
BuildRequires:	qt-devel >= 3.1.2-2
BuildRequires:	qscintilla-devel > 1.53-1
BuildRequires:	rpm-pythonprov
BuildRequires:	sip = %{version}
BuildRequires:	XFree86-OpenGL-devel

%pyrequires_eq	python
Requires:	OpenGL
Requires:	qscintilla > 1.53-1
Obsoletes:	%{module}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_sipfilesdir	/usr/share/sip

%description
PyQt is a set of Python bindings for the Qt toolkit. The bindings are
implemented as a set of Python modules: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable and qtxml, and contains 300 classes and over 5,750
functions and methods.

%description -l pl
PyQT to zbiór dowi±zañ do Qt dla Pythona. Dowi±zania zosta³y
zaimplementowane jako modu³y Pythona: qt, qtcanvas, qtgl, qtnetwork,
qtsql, qttable i qtxml - zawieraj± one 300 klas i ponad 5 750 funkcji
i metod.

%package devel
Summary:	Files needed to build other bindings based on Qt
Summary(pl):	Pliki potrzebne do budowania innych dowi±zañ bazowanych na Qt
Group:		Development/Languages/Python
Requires:	%{name} = %{version}
%requires_eq	sip

%description devel
Sip files needed to build other bindings for C++ classes that inherit from
any of the Qt classes (e.g. KDE or your own).

%description devel -l pl
Pliki sip potrzebne do budowania innych dowi±zañ do klas C++
dziedzicz±cych z dowolnej klasy Qt (np. KDE lub w³asnych).

%package examples
Summary:	Examples for PyQt
Summary(pl):	Przyklady do PyQt
Group:		Libraries/Python
Requires:	%{name} = %{version}

%description examples
Examples code demonstrating how to use the Python bindings for Qt.

%description examples -l pl
Przykladowy kod demonstruj±cy jak u¿ywaæ PyQT.

%prep
%setup -q -n %{module}-x11-gpl-%{version}

%build
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_bindir}}

echo 'yes' | python build.py \
        -c -q %{_prefix} -i %{_includedir}/qt -l qt-mt \
        -b $RPM_BUILD_ROOT%{_bindir} -n %{_includedir}/qt -o %{_libdir} -d $RPM_BUILD_ROOT%{py_sitedir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
cp -R examples3/* $RPM_BUILD_ROOT%{_examplesdir}/python/%{module}

install -d $RPM_BUILD_ROOT%{_sipfilesdir}
cp sip/* $RPM_BUILD_ROOT%{_sipfilesdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README THANKS doc/%{module}/*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{py_sitedir}/lib*.so*
%{py_sitedir}/*.py[co]

%files devel
%defattr(644,root,root,755)
%{_sipfilesdir}/*


%files examples
%defattr(644,root,root,755)
%{_examplesdir}/python/%{module}

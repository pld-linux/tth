Summary:	TTH is a LaTeX to HTML converter
Summary(pl):	Konwerter LaTeXa do HTML
Name:		tth
Version:	3.08
Release:	1
License:	Free for non-commercial use
Group:		Applications/Text
Source0:	http://hutchinson.belmont.ma.us/tth/tth-noncom/%{name}_C.tgz
URL:		http://hutchinson.belmont.ma.us/tth/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
TTH is a very good LaTeX to HTML conversion program.

%description -l pl
TTH jest programem do konwersji LaTeXa do HTML.

%prep
%setup -q -n tth_C

%build
%{__cc} %{rpmcflags} %{rpmldflags} -o tth tth.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install latex2gif ps2gif ps2png tth $RPM_BUILD_ROOT%{_bindir}
install tth.1 $RPM_BUILD_ROOT%{_mandir}/man1
echo ".so tth.1" > $RPM_BUILD_ROOT%{_mandir}/man1/ps2gif.1

gzip -9nf license.txt CHANGES

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc license.txt.gz CHANGES.gz tth_manual.html
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

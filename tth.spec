Summary:	TTH is a LaTeX to HTML converter.
Name:		tth
Version:	2.51
Release:	1
Copyright:	Free for non-commercial use.
Group:		Utilities/Text
Source:		tth_C.tgz
URL:		http://hutchinson.belmont.ma.us/tth/
BuildRoot:	/tmp/%{name}-%{version}-root

%description
TTH is a very good LaTeX to HTML conversion program.

%prep
%setup -q -n tth_C

%build
gcc -O2 -o tth tth.c

%install
rm -rf ${RPM_BUILD_ROOT}
install -d -m 755 ${RPM_BUILD_ROOT}/usr/bin
cp l2h latex2gif ps2gif ps2png tth ${RPM_BUILD_ROOT}/usr/bin

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%attr(-,root,root) %doc license.txt tth_manual.html CHANGES
%attr(-,root,root) /usr/bin/*

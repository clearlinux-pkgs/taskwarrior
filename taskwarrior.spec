#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : taskwarrior
Version  : 2.5.1
Release  : 5
URL      : https://taskwarrior.org/download/task-2.5.1.tar.gz
Source0  : https://taskwarrior.org/download/task-2.5.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: taskwarrior-bin = %{version}-%{release}
Requires: taskwarrior-license = %{version}-%{release}
Requires: taskwarrior-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : util-linux-dev

%description
Configure VIM for Syntax Highlighting of Taskwarrior Data
The task data files (pending.data, completed.data and undo.data),
configuration file (.taskrc) as well as edits made via commands like "task 1
edit" can be color-highlighted if you happen to use VIM as your preferred text
editor.  Eventually this will happen automatically in newer versions of VIM,
but for now you have to do a little bit of file shuffling.

%package bin
Summary: bin components for the taskwarrior package.
Group: Binaries
Requires: taskwarrior-license = %{version}-%{release}
Requires: taskwarrior-man = %{version}-%{release}

%description bin
bin components for the taskwarrior package.


%package doc
Summary: doc components for the taskwarrior package.
Group: Documentation
Requires: taskwarrior-man = %{version}-%{release}

%description doc
doc components for the taskwarrior package.


%package license
Summary: license components for the taskwarrior package.
Group: Default

%description license
license components for the taskwarrior package.


%package man
Summary: man components for the taskwarrior package.
Group: Default

%description man
man components for the taskwarrior package.


%prep
%setup -q -n task-2.5.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549646994
mkdir -p clr-build
pushd clr-build
%cmake .. -DCMAKE_BUILD_TYPE=release -DENABLE_SYNC=OFF
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1549646994
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/taskwarrior
cp COPYING %{buildroot}/usr/share/package-licenses/taskwarrior/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/taskwarrior/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/task

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/task/AUTHORS
/usr/share/doc/task/COPYING
/usr/share/doc/task/ChangeLog
/usr/share/doc/task/INSTALL
/usr/share/doc/task/LICENSE
/usr/share/doc/task/NEWS
/usr/share/doc/task/README.md
/usr/share/doc/task/rc/dark-16.theme
/usr/share/doc/task/rc/dark-256.theme
/usr/share/doc/task/rc/dark-blue-256.theme
/usr/share/doc/task/rc/dark-gray-256.theme
/usr/share/doc/task/rc/dark-gray-blue-256.theme
/usr/share/doc/task/rc/dark-green-256.theme
/usr/share/doc/task/rc/dark-red-256.theme
/usr/share/doc/task/rc/dark-violets-256.theme
/usr/share/doc/task/rc/dark-yellow-green.theme
/usr/share/doc/task/rc/holidays.be-BY.rc
/usr/share/doc/task/rc/holidays.cs-CZ.rc
/usr/share/doc/task/rc/holidays.da-DK.rc
/usr/share/doc/task/rc/holidays.de-AT.rc
/usr/share/doc/task/rc/holidays.de-BE.rc
/usr/share/doc/task/rc/holidays.de-CH.rc
/usr/share/doc/task/rc/holidays.de-DE.rc
/usr/share/doc/task/rc/holidays.el-GR.rc
/usr/share/doc/task/rc/holidays.en-AU.rc
/usr/share/doc/task/rc/holidays.en-CA.rc
/usr/share/doc/task/rc/holidays.en-GB.rc
/usr/share/doc/task/rc/holidays.en-GL.rc
/usr/share/doc/task/rc/holidays.en-HK.rc
/usr/share/doc/task/rc/holidays.en-IN.rc
/usr/share/doc/task/rc/holidays.en-NZ.rc
/usr/share/doc/task/rc/holidays.en-US.rc
/usr/share/doc/task/rc/holidays.en-ZA.rc
/usr/share/doc/task/rc/holidays.es-CO.rc
/usr/share/doc/task/rc/holidays.es-EC.rc
/usr/share/doc/task/rc/holidays.es-ES.rc
/usr/share/doc/task/rc/holidays.es-MX.rc
/usr/share/doc/task/rc/holidays.es-US.rc
/usr/share/doc/task/rc/holidays.et-EE.rc
/usr/share/doc/task/rc/holidays.fi-FI.rc
/usr/share/doc/task/rc/holidays.fr-BE.rc
/usr/share/doc/task/rc/holidays.fr-FR.rc
/usr/share/doc/task/rc/holidays.ga-IE.rc
/usr/share/doc/task/rc/holidays.hr-HR.rc
/usr/share/doc/task/rc/holidays.is-IS.rc
/usr/share/doc/task/rc/holidays.it-IT.rc
/usr/share/doc/task/rc/holidays.jp-JP.rc
/usr/share/doc/task/rc/holidays.lt-LT.rc
/usr/share/doc/task/rc/holidays.lv-LV.rc
/usr/share/doc/task/rc/holidays.nb-NO.rc
/usr/share/doc/task/rc/holidays.nb-SJ.rc
/usr/share/doc/task/rc/holidays.nl-BE.rc
/usr/share/doc/task/rc/holidays.nl-NL.rc
/usr/share/doc/task/rc/holidays.pl-PL.rc
/usr/share/doc/task/rc/holidays.por-PRT.rc
/usr/share/doc/task/rc/holidays.pt-BR.rc
/usr/share/doc/task/rc/holidays.pt-PT.rc
/usr/share/doc/task/rc/holidays.ru-RU.rc
/usr/share/doc/task/rc/holidays.sv-SE.rc
/usr/share/doc/task/rc/holidays.tr-TR.rc
/usr/share/doc/task/rc/light-16.theme
/usr/share/doc/task/rc/light-256.theme
/usr/share/doc/task/rc/no-color.theme
/usr/share/doc/task/rc/refresh
/usr/share/doc/task/rc/solarized-dark-256.theme
/usr/share/doc/task/rc/solarized-light-256.theme
/usr/share/doc/task/scripts/add-ons/README
/usr/share/doc/task/scripts/add-ons/update-holidays.pl
/usr/share/doc/task/scripts/bash/task.sh
/usr/share/doc/task/scripts/bash/task_functions.sh
/usr/share/doc/task/scripts/fish/task.fish
/usr/share/doc/task/scripts/hooks/README
/usr/share/doc/task/scripts/hooks/on-add
/usr/share/doc/task/scripts/hooks/on-add.the
/usr/share/doc/task/scripts/hooks/on-exit
/usr/share/doc/task/scripts/hooks/on-exit.shadow-file
/usr/share/doc/task/scripts/hooks/on-launch
/usr/share/doc/task/scripts/hooks/on-modify
/usr/share/doc/task/scripts/vim/README
/usr/share/doc/task/scripts/vim/ftdetect/task.vim
/usr/share/doc/task/scripts/vim/syntax/taskdata.vim
/usr/share/doc/task/scripts/vim/syntax/taskedit.vim
/usr/share/doc/task/scripts/vim/syntax/taskrc.vim
/usr/share/doc/task/scripts/zsh/_task
/usr/share/doc/task/task-ref.pdf

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/taskwarrior/COPYING
/usr/share/package-licenses/taskwarrior/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/task.1
/usr/share/man/man5/task-color.5
/usr/share/man/man5/task-sync.5
/usr/share/man/man5/taskrc.5

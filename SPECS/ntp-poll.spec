Summary: polling ntp server during boot process
Name: ntp-poll
Version: 1.0
Release: 1
Group: github 
BuildArch: noarch
Source: ntp-poll.tar
URL: http://www.dfs.de
Distribution: suse
Vendor: DFS Deutsche Flugsicherung GmbH, Langen, Germany
Packager: Valeri Windermut <valeri.windermut@dfs.de>
License: Valeri Windermut

%description
Init-script to achieve initial poll of ntp-servers. Operational environments generally must have
their ntp-servers synchronized before the application comes up. The user can choose the maximum
intervall of tries for the "sntp" command or cancel the programm by pressing "ctrl-c".

%prep
%setup -n ntp-poll

%install
mkdir -p $RPM_BUILD_ROOT
cp -a * $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/etc/init.d/ntp-poll
/etc/sysconfig/ntp_poll_info

%post
chkconfig ntp-poll on

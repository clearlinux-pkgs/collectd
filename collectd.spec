#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : collectd
Version  : 5.12.0
Release  : 24
URL      : https://storage.googleapis.com/collectd-tarballs/collectd-5.12.0.tar.bz2
Source0  : https://storage.googleapis.com/collectd-tarballs/collectd-5.12.0.tar.bz2
Summary  : barometer plugin for collectd
Group    : Development/Tools
License  : GPL-2.0 MIT
Requires: collectd-bin = %{version}-%{release}
Requires: collectd-data = %{version}-%{release}
Requires: collectd-lib = %{version}-%{release}
Requires: collectd-license = %{version}-%{release}
Requires: collectd-man = %{version}-%{release}
Requires: collectd-perl = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-cpan
BuildRequires : curl-dev
BuildRequires : flex
BuildRequires : jansson-dev
BuildRequires : libcap-dev
BuildRequires : libgcrypt-dev
BuildRequires : libmnl-dev
BuildRequires : libnotify-dev
BuildRequires : libpcap-dev
BuildRequires : librdkafka-dev
BuildRequires : openldap-dev
BuildRequires : openssl-dev
BuildRequires : perl(YAML::Any)
BuildRequires : pkgconfig(libmicrohttpd)
BuildRequires : pkgconfig(libprotobuf-c)
BuildRequires : pkgconfig(librrd)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(protobuf)
BuildRequires : python3-dev
BuildRequires : systemd-dev
BuildRequires : valgrind
BuildRequires : yajl-dev
Patch1: python311.patch

%description
collectd is a small daemon written in C for performance.  It reads various
system  statistics  and updates  RRD files,  creating  them if necessary.
Since the daemon doesn't need to startup every time it wants to update the
files it's very fast and easy on the system. Also, the statistics are very
fine grained since the files are updated every 10 seconds.

%package bin
Summary: bin components for the collectd package.
Group: Binaries
Requires: collectd-data = %{version}-%{release}
Requires: collectd-license = %{version}-%{release}

%description bin
bin components for the collectd package.


%package data
Summary: data components for the collectd package.
Group: Data

%description data
data components for the collectd package.


%package dev
Summary: dev components for the collectd package.
Group: Development
Requires: collectd-lib = %{version}-%{release}
Requires: collectd-bin = %{version}-%{release}
Requires: collectd-data = %{version}-%{release}
Provides: collectd-devel = %{version}-%{release}
Requires: collectd = %{version}-%{release}

%description dev
dev components for the collectd package.


%package lib
Summary: lib components for the collectd package.
Group: Libraries
Requires: collectd-data = %{version}-%{release}
Requires: collectd-license = %{version}-%{release}

%description lib
lib components for the collectd package.


%package license
Summary: license components for the collectd package.
Group: Default

%description license
license components for the collectd package.


%package man
Summary: man components for the collectd package.
Group: Default

%description man
man components for the collectd package.


%package perl
Summary: perl components for the collectd package.
Group: Default
Requires: collectd = %{version}-%{release}

%description perl
perl components for the collectd package.


%prep
%setup -q -n collectd-5.12.0
cd %{_builddir}/collectd-5.12.0
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666739186
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static --with-perl-bindings="PREFIX=/usr INSTALLDIRS=vendor NO_PACKLIST=true NO_PERLLOCAL=true"
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1666739186
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/collectd
cp %{_builddir}/collectd-%{version}/COPYING %{buildroot}/usr/share/package-licenses/collectd/93a4490e1756e10ae6f7a60183f1e1e895c22bcd || :
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/collectd
/usr/bin/collectd-nagios
/usr/bin/collectd-tg
/usr/bin/collectdctl
/usr/bin/collectdmon

%files data
%defattr(-,root,root,-)
/usr/share/collectd/postgresql_default.conf
/usr/share/collectd/types.db

%files dev
%defattr(-,root,root,-)
/usr/include/collectd/client.h
/usr/include/collectd/lcc_features.h
/usr/include/collectd/network.h
/usr/include/collectd/network_buffer.h
/usr/include/collectd/network_parse.h
/usr/include/collectd/server.h
/usr/include/collectd/types.h
/usr/lib64/libcollectdclient.so
/usr/lib64/pkgconfig/libcollectdclient.pc
/usr/share/man/man3/Collectd::Unixsock.3

%files lib
%defattr(-,root,root,-)
/usr/lib64/collectd/aggregation.so
/usr/lib64/collectd/apache.so
/usr/lib64/collectd/apcups.so
/usr/lib64/collectd/battery.so
/usr/lib64/collectd/buddyinfo.so
/usr/lib64/collectd/capabilities.so
/usr/lib64/collectd/ceph.so
/usr/lib64/collectd/cgroups.so
/usr/lib64/collectd/check_uptime.so
/usr/lib64/collectd/chrony.so
/usr/lib64/collectd/connectivity.so
/usr/lib64/collectd/conntrack.so
/usr/lib64/collectd/contextswitch.so
/usr/lib64/collectd/cpu.so
/usr/lib64/collectd/cpufreq.so
/usr/lib64/collectd/cpusleep.so
/usr/lib64/collectd/csv.so
/usr/lib64/collectd/curl.so
/usr/lib64/collectd/curl_json.so
/usr/lib64/collectd/df.so
/usr/lib64/collectd/disk.so
/usr/lib64/collectd/dns.so
/usr/lib64/collectd/dpdk_telemetry.so
/usr/lib64/collectd/drbd.so
/usr/lib64/collectd/email.so
/usr/lib64/collectd/entropy.so
/usr/lib64/collectd/ethstat.so
/usr/lib64/collectd/exec.so
/usr/lib64/collectd/fhcount.so
/usr/lib64/collectd/filecount.so
/usr/lib64/collectd/fscache.so
/usr/lib64/collectd/hddtemp.so
/usr/lib64/collectd/hugepages.so
/usr/lib64/collectd/infiniband.so
/usr/lib64/collectd/interface.so
/usr/lib64/collectd/ipc.so
/usr/lib64/collectd/ipvs.so
/usr/lib64/collectd/irq.so
/usr/lib64/collectd/load.so
/usr/lib64/collectd/log_logstash.so
/usr/lib64/collectd/logfile.so
/usr/lib64/collectd/logparser.so
/usr/lib64/collectd/lua.so
/usr/lib64/collectd/madwifi.so
/usr/lib64/collectd/match_empty_counter.so
/usr/lib64/collectd/match_hashed.so
/usr/lib64/collectd/match_regex.so
/usr/lib64/collectd/match_timediff.so
/usr/lib64/collectd/match_value.so
/usr/lib64/collectd/mbmon.so
/usr/lib64/collectd/mcelog.so
/usr/lib64/collectd/md.so
/usr/lib64/collectd/mdevents.so
/usr/lib64/collectd/memcached.so
/usr/lib64/collectd/memory.so
/usr/lib64/collectd/multimeter.so
/usr/lib64/collectd/netlink.so
/usr/lib64/collectd/network.so
/usr/lib64/collectd/nfs.so
/usr/lib64/collectd/nginx.so
/usr/lib64/collectd/notify_desktop.so
/usr/lib64/collectd/notify_nagios.so
/usr/lib64/collectd/ntpd.so
/usr/lib64/collectd/numa.so
/usr/lib64/collectd/olsrd.so
/usr/lib64/collectd/openldap.so
/usr/lib64/collectd/openvpn.so
/usr/lib64/collectd/ovs_events.so
/usr/lib64/collectd/ovs_stats.so
/usr/lib64/collectd/pcie_errors.so
/usr/lib64/collectd/perl.so
/usr/lib64/collectd/pinba.so
/usr/lib64/collectd/powerdns.so
/usr/lib64/collectd/processes.so
/usr/lib64/collectd/procevent.so
/usr/lib64/collectd/protocols.so
/usr/lib64/collectd/python.so
/usr/lib64/collectd/rrdcached.so
/usr/lib64/collectd/rrdtool.so
/usr/lib64/collectd/serial.so
/usr/lib64/collectd/statsd.so
/usr/lib64/collectd/swap.so
/usr/lib64/collectd/synproxy.so
/usr/lib64/collectd/sysevent.so
/usr/lib64/collectd/syslog.so
/usr/lib64/collectd/table.so
/usr/lib64/collectd/tail.so
/usr/lib64/collectd/tail_csv.so
/usr/lib64/collectd/target_notification.so
/usr/lib64/collectd/target_replace.so
/usr/lib64/collectd/target_scale.so
/usr/lib64/collectd/target_set.so
/usr/lib64/collectd/target_v5upgrade.so
/usr/lib64/collectd/tcpconns.so
/usr/lib64/collectd/teamspeak2.so
/usr/lib64/collectd/ted.so
/usr/lib64/collectd/thermal.so
/usr/lib64/collectd/threshold.so
/usr/lib64/collectd/turbostat.so
/usr/lib64/collectd/ubi.so
/usr/lib64/collectd/unixsock.so
/usr/lib64/collectd/uptime.so
/usr/lib64/collectd/users.so
/usr/lib64/collectd/uuid.so
/usr/lib64/collectd/vmem.so
/usr/lib64/collectd/vserver.so
/usr/lib64/collectd/wireless.so
/usr/lib64/collectd/write_graphite.so
/usr/lib64/collectd/write_http.so
/usr/lib64/collectd/write_influxdb_udp.so
/usr/lib64/collectd/write_kafka.so
/usr/lib64/collectd/write_log.so
/usr/lib64/collectd/write_prometheus.so
/usr/lib64/collectd/write_sensu.so
/usr/lib64/collectd/write_stackdriver.so
/usr/lib64/collectd/write_syslog.so
/usr/lib64/collectd/write_tsdb.so
/usr/lib64/collectd/zfs_arc.so
/usr/lib64/collectd/zookeeper.so
/usr/lib64/libcollectdclient.so.1
/usr/lib64/libcollectdclient.so.1.1.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/collectd/93a4490e1756e10ae6f7a60183f1e1e895c22bcd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/collectd-nagios.1
/usr/share/man/man1/collectd-tg.1
/usr/share/man/man1/collectd.1
/usr/share/man/man1/collectdctl.1
/usr/share/man/man1/collectdmon.1
/usr/share/man/man5/collectd-email.5
/usr/share/man/man5/collectd-exec.5
/usr/share/man/man5/collectd-java.5
/usr/share/man/man5/collectd-lua.5
/usr/share/man/man5/collectd-perl.5
/usr/share/man/man5/collectd-python.5
/usr/share/man/man5/collectd-snmp.5
/usr/share/man/man5/collectd-threshold.5
/usr/share/man/man5/collectd-unixsock.5
/usr/share/man/man5/collectd.conf.5
/usr/share/man/man5/types.db.5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*

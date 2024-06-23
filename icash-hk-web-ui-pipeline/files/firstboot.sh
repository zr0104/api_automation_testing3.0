# Check if the secondary NIC installed
ip addr show eth1
if [[ $? == 0 ]]
then echo "Secondary NIC installed"
    eth1ip=$(curl -sf "http:metadata.google.internal/computeMetadata/v1/instance/network-interface/1/ip" -H "Metadata-Flavor: Google")
    eth1gw=$(curl -sf "http:metadata.google.internal/computeMetadata/v1/instance/network-interface/1/gateway" -H "Metadata-Flavor: Google")
    echo "Secondary NIC IP address is: ${eth1ip}"
    echo "Secondary NIC gateway address is: ${eth1gw}"
    retryCountdown=6 && echo "Retry set to: ${retryCountdown} time"
    retryInterval=5 && echo "Retry interval set to: ${retryInterval}s"
    if [[ ${eth1gw} == 192.168.* ]]
  then echo -e "\nAdding static route..."
      for ((;;))
      do
         route add -net 192.168.0.0/16 gw ${eth1gw} dev eth1
         if [[ $? == 0 ]]
         then echo -e "Added successfully.\n"
              sleep 5 && break
              if [[ ${retryCountdown} -gt 0 ]]
              then echo -e "\nAdding failed, wait for ${retryInterval}s and retry."
                   sleep ${retryInterval} && retryCountdown=$[${retryCountdown}-1]
                   echo "Retrying (remain ${retryCountdown} times)."
              else echo -e "/nRetry failed, please check details logs.\n" && break
              fi
         fi
      done
  else echo "IP range is NOT inside 192.168.0.0/16"
  fi
  route -n > /temp/route-output && cat /temp/route-output
else echo "Secondary NIC NOT installed"
fi

sleep 100

IpEth0=`ifconfig eth0 | grep "inet" | cut -f 10 -d " "`

rm -rf /lib/systemd/system/service-automation-test.service

echo ${IpEth0} | grep "^10\.91"
if [ $? -eq 0 ];then
    cp -a /opt/icash-hk-gcp-backend-system/service-automation-test.service /lib/systemd/systemd/service-automation-test.service
fi

echo ${IpEth0} | grep "^10\.92"
if [ $? -eq 0 ];then
    cp -a /opt/icash-hk-gcp-backend-system/service-automation-test.service /lib/systemd/systemd/service-automation-test.service
fi


systemctl start service-automation-test


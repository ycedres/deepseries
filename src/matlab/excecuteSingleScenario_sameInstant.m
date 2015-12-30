clear
wSizeStart = 10;
wSizeEnd = 14;
         
file = 'minutal_data_sameInstantOfDay_wStart10_wEnd14_h24.mat'

path = strcat('../../data/',file)
load(path)
performanceArray=[];

for i=wSizeStart:wSizeEnd
    inputs = eval(strcat('k_',int2str(i),'_inputs'));
    outputs = eval(strcat('k_',int2str(i),'_outputs'));
    nn1;
    y=net(inputs);
    %performanceArray_mse(i)=performance;
    %performanceArray_crossentropy(i)= crossentropy(net,outputs,y);
    performanceArray_crossentropy(i)= performance_crossentropy;
    %save(strcat('resultados_consecutiveDays_',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
    %clear save(strcat('resultados',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
    clear inputs
    clear outputs
end

x=linspace(wSizeStart,wSizeEnd,wSizeEnd-wSizeStart+1);
%perfArray_mse = performanceArray_mse(wSizeStart:wSizeEnd);
perfArray_crossentropy = performanceArray_crossentropy(wSizeStart:wSizeEnd);
%figure
%plot(x,perfArray)
%xlabel('Window Size')
%ylabel('Performance')

%table_mse=[x',perfArray_mse'];
table_crossentropy=[x',perfArray_crossentropy'];
%save(strcat('perfTable_',int2str(wSizeStart),'_',int2str(wSizeEnd)),'table')

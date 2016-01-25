clear
wSizeStart = 10;
wSizeEnd = 14;
         
file = 'minutal_data_sameInstantOfDay_wStart45_wEnd49_h24.mat'

path = strcat('../../data/',file)
load(path)
performanceArray=[];
table_matrix = cell(1,10);
for tm=1:10
    for i=wSizeStart:wSizeEnd
        inputs = eval(strcat('k_',int2str(i),'_inputs'));
        outputs = eval(strcat('k_',int2str(i),'_outputs'));
        nn1;
        performanceArray(i)=performance;
        %save(strcat('resultados_consecutiveDays_',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
        %clear save(strcat('resultados',int2str(i)),'errors','hiddenLayerSize','net','performance','targets','tr')
        clear inputs
        clear outputs
    end

    x=linspace(wSizeStart,wSizeEnd,wSizeEnd-wSizeStart+1);
    perfArray = performanceArray(wSizeStart:wSizeEnd);
    %figure
    %plot(x,perfArray)
    %xlabel('Window Size')
    %ylabel('Performance')

    table=[x',perfArray'];
    table_matrix{tm} = table;
    %save(strcat('perfTable_',int2str(wSizeStart),'_',int2str(wSizeEnd)),'table')
end

save('table_matrix.mat','table_matrix')

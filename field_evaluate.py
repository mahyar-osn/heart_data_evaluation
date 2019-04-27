from __future__ import division

import os
import sys

import numpy as np

from opencmiss.zinc.context import Context
from opencmiss.zinc.status import OK as ZINC_OK


subjects = ['50', '52', '53', '59']
for subject in subjects:
    root = '/hpc/nebr002/Fitting/Fit/FieldFitting/Data'
    fieldNames = ['Anisotropy', 'Area3d', 'Elongation', 'EqDiameter', 'FeretShape3d', 'Length3d', 'Orientation2Phi',
                  'Orientation2Theta', 'OrientationPhi', 'OrientationTheta', 'Perimeter', 'Shape_VA3d', 'Volume3d',
                  'Width3d']

    for fieldName in fieldNames:
        filepath = os.path.join(root, subject, fieldName, 'FieldFit')
        context = Context("Field")
        region = context.getDefaultRegion()
        if not os.path.exists(os.path.join(filepath, 'fitted_field.exnode')):
            continue
        region.readFile(os.path.join(filepath, 'fitted_field.exnode'))
        region.readFile(os.path.join(filepath, 'fitted_field.exelem'))
        fieldmodule = region.getFieldmodule()
        field = fieldmodule.findFieldByName("general")
        cache = fieldmodule.createFieldcache()
        mesh = fieldmodule.findMeshByDimension(3)
        elementIterator = mesh.createElementiterator()
        element = elementIterator.next()

        fieldList = list()
        fieldNum = list()
        elemList = list()
        xi1List = list()
        xi2List = list()

        gridSize = 10

        counter = 1
        for xi_1 in range(0, gridSize):
            for xi_2 in range(0, gridSize):
                xi = [xi_1 / gridSize, xi_2 / gridSize, 0]
                if not element.isValid():
                    del elementIterator
                    elementIterator = mesh.createElementiterator()
                    element = elementIterator.next()
                while element.isValid():
                    cache.setMeshLocation(element, xi)
                    result, outValues = field.evaluateReal(cache, 3)
                    if result == ZINC_OK:
                        print(element.getIdentifier(), outValues)
                        elemList.append(element.getIdentifier())
                        fieldList.append(outValues[0])
                    else:
                        break
                    xi1List.append(xi[0])
                    xi2List.append(xi[1])
                    element = elementIterator.next()
                    fieldNum.append(counter)
                    counter += 1

        fieldcsvarray = list(zip(fieldNum, xi1List, xi2List, fieldList, elemList))
        fieldValues = np.asarray(fieldcsvarray)
        outputpath = os.path.join(root, subject, fieldName, 'FieldFit')
        np.savetxt(os.path.join(outputpath, 'evaluated_field_elements_included.csv'), fieldValues,
                   ['%i', '%.1f', '%.1f', '%.4f', '%i'], delimiter=',')

        print('Field = ', fieldName)

print('done')

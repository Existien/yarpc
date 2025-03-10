/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/06_enums.yml
 *   Template: qt6/types_header.j2
 */
#pragma once
#include <qqmlintegration.h>
#include <QObject>
#include "EnumStruct.hpp"
#include "Color.hpp"

namespace gen::enums {

/**
* @brief Registers MetaTypes used by this interface.
*/
void registerMetaTypes();


/**
 * Provides JS -> QMap conversion functions in QML.
 *
 * Since JS objects are passed as QJSValue,
 * we need some helper functions to convert them
 * to the QMaps used in the interface.
 *
 * This class provides helper functions to convert
 * JS objects and array to the types required by
 * the interface.
 */
class Conversions : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON
public:
    Q_INVOKABLE QMap<Color::Type, Color::Type> jsToMapOfColorToColor(QVariant jsonObject);
};
}
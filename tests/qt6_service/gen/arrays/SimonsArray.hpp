/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/04.2_arrays_with_structs.yml
 *   Object: SimonsArray
 *   Template: qt6/struct_header.j2
 */

#pragma once
#include "StructArray.hpp"
#include <QObject>
#include <QDBusArgument>
#include <QDBusMessage>
#include <qqmlintegration.h>

namespace gen::arrays {

/**
 * @brief A struct containing arrays
 */
struct SimonsArray {
    Q_GADGET
    /**
     * @brief some struct arrays
     */
    Q_PROPERTY(QList<StructArray> numbers MEMBER numbers)
public:
    /**
     * @brief some struct arrays
     */
    QList<StructArray> numbers;
};

/**
 * @brief Marshalls a SimonsArray into a QDBusArgument.
 *
 * @param argument the argument to marshall into
 * @param object the object to marshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
QDBusArgument &operator<<(QDBusArgument &argument, const SimonsArray &object);

/**
 * @brief Demarshalls a SimonsArray from a QDBusArgument.
 *
 * @param argument the argument to demarshall from
 * @param object the object to demarshall
 *
 * @returns QDBusArgument the argument containing the marshalled object (same as argument)
 */
const QDBusArgument &operator>>(const QDBusArgument &argument, SimonsArray &object);

bool operator!=(const SimonsArray &lhs, const SimonsArray &rhs);

bool operator!=(const QList<SimonsArray> &lhs, const QList<SimonsArray> &rhs);

/**
 * @brief Factory to create SimonsArray objects in QML.
 */
class SimonsArrayFactory : public QObject {
    Q_OBJECT
    QML_ELEMENT
    QML_SINGLETON
public:
    /**
     * @brief Create a SimonsArray object.
     *
     * @param numbers some struct arrays
     */
    SimonsArray create (
        QList<StructArray> numbers
    ) const;

    /**
     * @brief Create a SimonsArray object.
     *
     * @param numbers some struct arrays
     */
    Q_INVOKABLE SimonsArray create (
        QVariant numbers
    ) const;
};

}

Q_DECLARE_METATYPE(gen::arrays::SimonsArray)